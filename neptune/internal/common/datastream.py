#
# Copyright (c) 2017, deepsense.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import hashlib
import os
import stat
import tarfile

from future.builtins import object

import io


class FileChunkWithCallback(object):
    def __init__(self, fobj, start, end, callback):
        self.fobj = fobj
        self.callback = callback
        self.start = start
        self.end = end

    def get_data(self):
        self.fobj.seek(self.start)
        item = self.fobj.read(self.end - self.start)
        if isinstance(item, Exception):
            raise item
        self.callback(len(item))
        return item

    def skip(self):
        self.callback(self.end - self.start)

    def md5(self):
        hash_md5 = hashlib.md5()
        self.fobj.seek(self.start)
        item = self.fobj.read(self.end - self.start)
        if isinstance(item, Exception):
            raise item
        hash_md5.update(item)
        return hash_md5.hexdigest()


def dummy(*_):
    pass


class FileChunkStream(object):

    def __init__(self, upload_entry, callback=dummy):
        self.filename = upload_entry.target_path
        self.callback = callback
        self.fobj = io.open(upload_entry.source_path, "rb")
        self.length = os.path.getsize(upload_entry.source_path)
        self.permissions = self.permissions_to_unix_string(upload_entry.source_path)

    @classmethod
    def permissions_to_unix_string(cls, path):
        st = 0
        if os.path.exists(path):
            st = os.lstat(path).st_mode
        is_dir = 'd' if stat.S_ISDIR(st) else '-'
        dic = {'7': 'rwx', '6': 'rw-', '5': 'r-x', '4': 'r--', '3': '-wx', '2': '-w-', '1': '--x', '0': '---'}
        perm = ("%03o" % st)[-3:]
        return is_dir + ''.join(dic.get(x, x) for x in perm)

    def __eq__(self, fs):
        if isinstance(self, fs.__class__):
            return self.__dict__ == fs.__dict__
        return False

    def generate(self, chunk_size=1 * 1024 * 1024):
        num_chunks = (self.length + chunk_size - 1) // chunk_size
        if num_chunks == 0:
            yield FileChunkWithCallback(self.fobj, 0, 0, self.callback)

        for i in range(num_chunks):
            start = i * chunk_size
            end = min(self.length, (i + 1) * chunk_size)
            yield FileChunkWithCallback(self.fobj, start, end, self.callback)

    def close(self):
        self.fobj.close()


def compress_to_tar_gz_in_memory(upload_entries):
    f = io.BytesIO(b'')

    with tarfile.TarFile.open(fileobj=f, mode='w|gz', dereference=True) as archive:
        for entry in upload_entries:
            archive.add(name=entry.source_path, arcname=entry.target_path, recursive=False)

    f.seek(0)
    data = f.read()
    return data
