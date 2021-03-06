# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class QueueEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anonymous_page_view=None, apply_fee=None, cancel_account=None, change_credit_card=None, change_pricing_plan=None, cli_usage=None, contact_email=None, contact_notification=None, contact_us=None, create_account=None, create_project=None, downgrade=None, download_storage_event=None, experiment_ends=None, experiment_inits=None, experiment_runs=None, failed_charge_card=None, getting_started_experiment_ends=None, interact_chartset=None, membership_change=None, modify_balance=None, modify_chartset=None, modify_filter=None, modify_leaderboard=None, neptune_crash=None, quota_update=None, read_documentation=None, remove_project=None, remove_storage_event=None, rename_project=None, schedule_experiment=None, successful_charge_card=None, time_spent=None, trial_ends=None, upload_storage_event=None, user_id=None, user_page_view=None):
        """
        QueueEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anonymous_page_view': 'AnonymousPageViewEvent',
            'apply_fee': 'ApplyFeeEvent',
            'cancel_account': 'CancelAccountEvent',
            'change_credit_card': 'ChangeCreditCardEvent',
            'change_pricing_plan': 'ChangePricingPlanEvent',
            'cli_usage': 'CliUsageEvent',
            'contact_email': 'ContactEmailEvent',
            'contact_notification': 'ContactNotificationEvent',
            'contact_us': 'ContactUsEvent',
            'create_account': 'CreateAccountEvent',
            'create_project': 'CreateProjectEvent',
            'downgrade': 'DowngradeEvent',
            'download_storage_event': 'DownloadStorageEvent',
            'experiment_ends': 'ExperimentEndsEvent',
            'experiment_inits': 'ExperimentInitsEvent',
            'experiment_runs': 'ExperimentRunsEvent',
            'failed_charge_card': 'FailedChargeCardEvent',
            'getting_started_experiment_ends': 'GettingStartedExperimentEndsEvent',
            'interact_chartset': 'InteractChartEvent',
            'membership_change': 'MembershipChangeEvent',
            'modify_balance': 'ModifyBalanceEvent',
            'modify_chartset': 'ModifyChartsetEvent',
            'modify_filter': 'ModifyFilterEvent',
            'modify_leaderboard': 'ModifyLeaderboardEvent',
            'neptune_crash': 'NeptuneCrashEvent',
            'quota_update': 'QuotaUpdateEvent',
            'read_documentation': 'ReadDocumentationEvent',
            'remove_project': 'RemoveProjectEvent',
            'remove_storage_event': 'RemoveStorageEvent',
            'rename_project': 'RenameProjectEvent',
            'schedule_experiment': 'ScheduleExperimentEvent',
            'successful_charge_card': 'SuccessfulChargeCardEvent',
            'time_spent': 'TimeSpentEvent',
            'trial_ends': 'TrialEndsEvent',
            'upload_storage_event': 'UploadStorageEvent',
            'user_id': 'str',
            'user_page_view': 'UserPageViewEvent'
        }

        self.attribute_map = {
            'anonymous_page_view': 'anonymousPageView',
            'apply_fee': 'applyFee',
            'cancel_account': 'cancelAccount',
            'change_credit_card': 'changeCreditCard',
            'change_pricing_plan': 'changePricingPlan',
            'cli_usage': 'cliUsage',
            'contact_email': 'contactEmail',
            'contact_notification': 'contactNotification',
            'contact_us': 'contactUs',
            'create_account': 'createAccount',
            'create_project': 'createProject',
            'downgrade': 'downgrade',
            'download_storage_event': 'downloadStorageEvent',
            'experiment_ends': 'experimentEnds',
            'experiment_inits': 'experimentInits',
            'experiment_runs': 'experimentRuns',
            'failed_charge_card': 'failedChargeCard',
            'getting_started_experiment_ends': 'gettingStartedExperimentEnds',
            'interact_chartset': 'interactChartset',
            'membership_change': 'membershipChange',
            'modify_balance': 'modifyBalance',
            'modify_chartset': 'modifyChartset',
            'modify_filter': 'modifyFilter',
            'modify_leaderboard': 'modifyLeaderboard',
            'neptune_crash': 'neptuneCrash',
            'quota_update': 'quotaUpdate',
            'read_documentation': 'readDocumentation',
            'remove_project': 'removeProject',
            'remove_storage_event': 'removeStorageEvent',
            'rename_project': 'renameProject',
            'schedule_experiment': 'scheduleExperiment',
            'successful_charge_card': 'successfulChargeCard',
            'time_spent': 'timeSpent',
            'trial_ends': 'trialEnds',
            'upload_storage_event': 'uploadStorageEvent',
            'user_id': 'userId',
            'user_page_view': 'userPageView'
        }

        self._anonymous_page_view = anonymous_page_view
        self._apply_fee = apply_fee
        self._cancel_account = cancel_account
        self._change_credit_card = change_credit_card
        self._change_pricing_plan = change_pricing_plan
        self._cli_usage = cli_usage
        self._contact_email = contact_email
        self._contact_notification = contact_notification
        self._contact_us = contact_us
        self._create_account = create_account
        self._create_project = create_project
        self._downgrade = downgrade
        self._download_storage_event = download_storage_event
        self._experiment_ends = experiment_ends
        self._experiment_inits = experiment_inits
        self._experiment_runs = experiment_runs
        self._failed_charge_card = failed_charge_card
        self._getting_started_experiment_ends = getting_started_experiment_ends
        self._interact_chartset = interact_chartset
        self._membership_change = membership_change
        self._modify_balance = modify_balance
        self._modify_chartset = modify_chartset
        self._modify_filter = modify_filter
        self._modify_leaderboard = modify_leaderboard
        self._neptune_crash = neptune_crash
        self._quota_update = quota_update
        self._read_documentation = read_documentation
        self._remove_project = remove_project
        self._remove_storage_event = remove_storage_event
        self._rename_project = rename_project
        self._schedule_experiment = schedule_experiment
        self._successful_charge_card = successful_charge_card
        self._time_spent = time_spent
        self._trial_ends = trial_ends
        self._upload_storage_event = upload_storage_event
        self._user_id = user_id
        self._user_page_view = user_page_view

    @property
    def anonymous_page_view(self):
        """
        Gets the anonymous_page_view of this QueueEvent.


        :return: The anonymous_page_view of this QueueEvent.
        :rtype: AnonymousPageViewEvent
        """
        return self._anonymous_page_view

    @anonymous_page_view.setter
    def anonymous_page_view(self, anonymous_page_view):
        """
        Sets the anonymous_page_view of this QueueEvent.


        :param anonymous_page_view: The anonymous_page_view of this QueueEvent.
        :type: AnonymousPageViewEvent
        """
        
        self._anonymous_page_view = anonymous_page_view

    @property
    def apply_fee(self):
        """
        Gets the apply_fee of this QueueEvent.


        :return: The apply_fee of this QueueEvent.
        :rtype: ApplyFeeEvent
        """
        return self._apply_fee

    @apply_fee.setter
    def apply_fee(self, apply_fee):
        """
        Sets the apply_fee of this QueueEvent.


        :param apply_fee: The apply_fee of this QueueEvent.
        :type: ApplyFeeEvent
        """
        
        self._apply_fee = apply_fee

    @property
    def cancel_account(self):
        """
        Gets the cancel_account of this QueueEvent.


        :return: The cancel_account of this QueueEvent.
        :rtype: CancelAccountEvent
        """
        return self._cancel_account

    @cancel_account.setter
    def cancel_account(self, cancel_account):
        """
        Sets the cancel_account of this QueueEvent.


        :param cancel_account: The cancel_account of this QueueEvent.
        :type: CancelAccountEvent
        """
        
        self._cancel_account = cancel_account

    @property
    def change_credit_card(self):
        """
        Gets the change_credit_card of this QueueEvent.


        :return: The change_credit_card of this QueueEvent.
        :rtype: ChangeCreditCardEvent
        """
        return self._change_credit_card

    @change_credit_card.setter
    def change_credit_card(self, change_credit_card):
        """
        Sets the change_credit_card of this QueueEvent.


        :param change_credit_card: The change_credit_card of this QueueEvent.
        :type: ChangeCreditCardEvent
        """
        
        self._change_credit_card = change_credit_card

    @property
    def change_pricing_plan(self):
        """
        Gets the change_pricing_plan of this QueueEvent.


        :return: The change_pricing_plan of this QueueEvent.
        :rtype: ChangePricingPlanEvent
        """
        return self._change_pricing_plan

    @change_pricing_plan.setter
    def change_pricing_plan(self, change_pricing_plan):
        """
        Sets the change_pricing_plan of this QueueEvent.


        :param change_pricing_plan: The change_pricing_plan of this QueueEvent.
        :type: ChangePricingPlanEvent
        """
        
        self._change_pricing_plan = change_pricing_plan

    @property
    def cli_usage(self):
        """
        Gets the cli_usage of this QueueEvent.


        :return: The cli_usage of this QueueEvent.
        :rtype: CliUsageEvent
        """
        return self._cli_usage

    @cli_usage.setter
    def cli_usage(self, cli_usage):
        """
        Sets the cli_usage of this QueueEvent.


        :param cli_usage: The cli_usage of this QueueEvent.
        :type: CliUsageEvent
        """
        
        self._cli_usage = cli_usage

    @property
    def contact_email(self):
        """
        Gets the contact_email of this QueueEvent.


        :return: The contact_email of this QueueEvent.
        :rtype: ContactEmailEvent
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """
        Sets the contact_email of this QueueEvent.


        :param contact_email: The contact_email of this QueueEvent.
        :type: ContactEmailEvent
        """
        
        self._contact_email = contact_email

    @property
    def contact_notification(self):
        """
        Gets the contact_notification of this QueueEvent.


        :return: The contact_notification of this QueueEvent.
        :rtype: ContactNotificationEvent
        """
        return self._contact_notification

    @contact_notification.setter
    def contact_notification(self, contact_notification):
        """
        Sets the contact_notification of this QueueEvent.


        :param contact_notification: The contact_notification of this QueueEvent.
        :type: ContactNotificationEvent
        """
        
        self._contact_notification = contact_notification

    @property
    def contact_us(self):
        """
        Gets the contact_us of this QueueEvent.


        :return: The contact_us of this QueueEvent.
        :rtype: ContactUsEvent
        """
        return self._contact_us

    @contact_us.setter
    def contact_us(self, contact_us):
        """
        Sets the contact_us of this QueueEvent.


        :param contact_us: The contact_us of this QueueEvent.
        :type: ContactUsEvent
        """
        
        self._contact_us = contact_us

    @property
    def create_account(self):
        """
        Gets the create_account of this QueueEvent.


        :return: The create_account of this QueueEvent.
        :rtype: CreateAccountEvent
        """
        return self._create_account

    @create_account.setter
    def create_account(self, create_account):
        """
        Sets the create_account of this QueueEvent.


        :param create_account: The create_account of this QueueEvent.
        :type: CreateAccountEvent
        """
        
        self._create_account = create_account

    @property
    def create_project(self):
        """
        Gets the create_project of this QueueEvent.


        :return: The create_project of this QueueEvent.
        :rtype: CreateProjectEvent
        """
        return self._create_project

    @create_project.setter
    def create_project(self, create_project):
        """
        Sets the create_project of this QueueEvent.


        :param create_project: The create_project of this QueueEvent.
        :type: CreateProjectEvent
        """
        
        self._create_project = create_project

    @property
    def downgrade(self):
        """
        Gets the downgrade of this QueueEvent.


        :return: The downgrade of this QueueEvent.
        :rtype: DowngradeEvent
        """
        return self._downgrade

    @downgrade.setter
    def downgrade(self, downgrade):
        """
        Sets the downgrade of this QueueEvent.


        :param downgrade: The downgrade of this QueueEvent.
        :type: DowngradeEvent
        """
        
        self._downgrade = downgrade

    @property
    def download_storage_event(self):
        """
        Gets the download_storage_event of this QueueEvent.


        :return: The download_storage_event of this QueueEvent.
        :rtype: DownloadStorageEvent
        """
        return self._download_storage_event

    @download_storage_event.setter
    def download_storage_event(self, download_storage_event):
        """
        Sets the download_storage_event of this QueueEvent.


        :param download_storage_event: The download_storage_event of this QueueEvent.
        :type: DownloadStorageEvent
        """
        
        self._download_storage_event = download_storage_event

    @property
    def experiment_ends(self):
        """
        Gets the experiment_ends of this QueueEvent.


        :return: The experiment_ends of this QueueEvent.
        :rtype: ExperimentEndsEvent
        """
        return self._experiment_ends

    @experiment_ends.setter
    def experiment_ends(self, experiment_ends):
        """
        Sets the experiment_ends of this QueueEvent.


        :param experiment_ends: The experiment_ends of this QueueEvent.
        :type: ExperimentEndsEvent
        """
        
        self._experiment_ends = experiment_ends

    @property
    def experiment_inits(self):
        """
        Gets the experiment_inits of this QueueEvent.


        :return: The experiment_inits of this QueueEvent.
        :rtype: ExperimentInitsEvent
        """
        return self._experiment_inits

    @experiment_inits.setter
    def experiment_inits(self, experiment_inits):
        """
        Sets the experiment_inits of this QueueEvent.


        :param experiment_inits: The experiment_inits of this QueueEvent.
        :type: ExperimentInitsEvent
        """
        
        self._experiment_inits = experiment_inits

    @property
    def experiment_runs(self):
        """
        Gets the experiment_runs of this QueueEvent.


        :return: The experiment_runs of this QueueEvent.
        :rtype: ExperimentRunsEvent
        """
        return self._experiment_runs

    @experiment_runs.setter
    def experiment_runs(self, experiment_runs):
        """
        Sets the experiment_runs of this QueueEvent.


        :param experiment_runs: The experiment_runs of this QueueEvent.
        :type: ExperimentRunsEvent
        """
        
        self._experiment_runs = experiment_runs

    @property
    def failed_charge_card(self):
        """
        Gets the failed_charge_card of this QueueEvent.


        :return: The failed_charge_card of this QueueEvent.
        :rtype: FailedChargeCardEvent
        """
        return self._failed_charge_card

    @failed_charge_card.setter
    def failed_charge_card(self, failed_charge_card):
        """
        Sets the failed_charge_card of this QueueEvent.


        :param failed_charge_card: The failed_charge_card of this QueueEvent.
        :type: FailedChargeCardEvent
        """
        
        self._failed_charge_card = failed_charge_card

    @property
    def getting_started_experiment_ends(self):
        """
        Gets the getting_started_experiment_ends of this QueueEvent.


        :return: The getting_started_experiment_ends of this QueueEvent.
        :rtype: GettingStartedExperimentEndsEvent
        """
        return self._getting_started_experiment_ends

    @getting_started_experiment_ends.setter
    def getting_started_experiment_ends(self, getting_started_experiment_ends):
        """
        Sets the getting_started_experiment_ends of this QueueEvent.


        :param getting_started_experiment_ends: The getting_started_experiment_ends of this QueueEvent.
        :type: GettingStartedExperimentEndsEvent
        """
        
        self._getting_started_experiment_ends = getting_started_experiment_ends

    @property
    def interact_chartset(self):
        """
        Gets the interact_chartset of this QueueEvent.


        :return: The interact_chartset of this QueueEvent.
        :rtype: InteractChartEvent
        """
        return self._interact_chartset

    @interact_chartset.setter
    def interact_chartset(self, interact_chartset):
        """
        Sets the interact_chartset of this QueueEvent.


        :param interact_chartset: The interact_chartset of this QueueEvent.
        :type: InteractChartEvent
        """
        
        self._interact_chartset = interact_chartset

    @property
    def membership_change(self):
        """
        Gets the membership_change of this QueueEvent.


        :return: The membership_change of this QueueEvent.
        :rtype: MembershipChangeEvent
        """
        return self._membership_change

    @membership_change.setter
    def membership_change(self, membership_change):
        """
        Sets the membership_change of this QueueEvent.


        :param membership_change: The membership_change of this QueueEvent.
        :type: MembershipChangeEvent
        """
        
        self._membership_change = membership_change

    @property
    def modify_balance(self):
        """
        Gets the modify_balance of this QueueEvent.


        :return: The modify_balance of this QueueEvent.
        :rtype: ModifyBalanceEvent
        """
        return self._modify_balance

    @modify_balance.setter
    def modify_balance(self, modify_balance):
        """
        Sets the modify_balance of this QueueEvent.


        :param modify_balance: The modify_balance of this QueueEvent.
        :type: ModifyBalanceEvent
        """
        
        self._modify_balance = modify_balance

    @property
    def modify_chartset(self):
        """
        Gets the modify_chartset of this QueueEvent.


        :return: The modify_chartset of this QueueEvent.
        :rtype: ModifyChartsetEvent
        """
        return self._modify_chartset

    @modify_chartset.setter
    def modify_chartset(self, modify_chartset):
        """
        Sets the modify_chartset of this QueueEvent.


        :param modify_chartset: The modify_chartset of this QueueEvent.
        :type: ModifyChartsetEvent
        """
        
        self._modify_chartset = modify_chartset

    @property
    def modify_filter(self):
        """
        Gets the modify_filter of this QueueEvent.


        :return: The modify_filter of this QueueEvent.
        :rtype: ModifyFilterEvent
        """
        return self._modify_filter

    @modify_filter.setter
    def modify_filter(self, modify_filter):
        """
        Sets the modify_filter of this QueueEvent.


        :param modify_filter: The modify_filter of this QueueEvent.
        :type: ModifyFilterEvent
        """
        
        self._modify_filter = modify_filter

    @property
    def modify_leaderboard(self):
        """
        Gets the modify_leaderboard of this QueueEvent.


        :return: The modify_leaderboard of this QueueEvent.
        :rtype: ModifyLeaderboardEvent
        """
        return self._modify_leaderboard

    @modify_leaderboard.setter
    def modify_leaderboard(self, modify_leaderboard):
        """
        Sets the modify_leaderboard of this QueueEvent.


        :param modify_leaderboard: The modify_leaderboard of this QueueEvent.
        :type: ModifyLeaderboardEvent
        """
        
        self._modify_leaderboard = modify_leaderboard

    @property
    def neptune_crash(self):
        """
        Gets the neptune_crash of this QueueEvent.


        :return: The neptune_crash of this QueueEvent.
        :rtype: NeptuneCrashEvent
        """
        return self._neptune_crash

    @neptune_crash.setter
    def neptune_crash(self, neptune_crash):
        """
        Sets the neptune_crash of this QueueEvent.


        :param neptune_crash: The neptune_crash of this QueueEvent.
        :type: NeptuneCrashEvent
        """
        
        self._neptune_crash = neptune_crash

    @property
    def quota_update(self):
        """
        Gets the quota_update of this QueueEvent.


        :return: The quota_update of this QueueEvent.
        :rtype: QuotaUpdateEvent
        """
        return self._quota_update

    @quota_update.setter
    def quota_update(self, quota_update):
        """
        Sets the quota_update of this QueueEvent.


        :param quota_update: The quota_update of this QueueEvent.
        :type: QuotaUpdateEvent
        """
        
        self._quota_update = quota_update

    @property
    def read_documentation(self):
        """
        Gets the read_documentation of this QueueEvent.


        :return: The read_documentation of this QueueEvent.
        :rtype: ReadDocumentationEvent
        """
        return self._read_documentation

    @read_documentation.setter
    def read_documentation(self, read_documentation):
        """
        Sets the read_documentation of this QueueEvent.


        :param read_documentation: The read_documentation of this QueueEvent.
        :type: ReadDocumentationEvent
        """
        
        self._read_documentation = read_documentation

    @property
    def remove_project(self):
        """
        Gets the remove_project of this QueueEvent.


        :return: The remove_project of this QueueEvent.
        :rtype: RemoveProjectEvent
        """
        return self._remove_project

    @remove_project.setter
    def remove_project(self, remove_project):
        """
        Sets the remove_project of this QueueEvent.


        :param remove_project: The remove_project of this QueueEvent.
        :type: RemoveProjectEvent
        """
        
        self._remove_project = remove_project

    @property
    def remove_storage_event(self):
        """
        Gets the remove_storage_event of this QueueEvent.


        :return: The remove_storage_event of this QueueEvent.
        :rtype: RemoveStorageEvent
        """
        return self._remove_storage_event

    @remove_storage_event.setter
    def remove_storage_event(self, remove_storage_event):
        """
        Sets the remove_storage_event of this QueueEvent.


        :param remove_storage_event: The remove_storage_event of this QueueEvent.
        :type: RemoveStorageEvent
        """
        
        self._remove_storage_event = remove_storage_event

    @property
    def rename_project(self):
        """
        Gets the rename_project of this QueueEvent.


        :return: The rename_project of this QueueEvent.
        :rtype: RenameProjectEvent
        """
        return self._rename_project

    @rename_project.setter
    def rename_project(self, rename_project):
        """
        Sets the rename_project of this QueueEvent.


        :param rename_project: The rename_project of this QueueEvent.
        :type: RenameProjectEvent
        """
        
        self._rename_project = rename_project

    @property
    def schedule_experiment(self):
        """
        Gets the schedule_experiment of this QueueEvent.


        :return: The schedule_experiment of this QueueEvent.
        :rtype: ScheduleExperimentEvent
        """
        return self._schedule_experiment

    @schedule_experiment.setter
    def schedule_experiment(self, schedule_experiment):
        """
        Sets the schedule_experiment of this QueueEvent.


        :param schedule_experiment: The schedule_experiment of this QueueEvent.
        :type: ScheduleExperimentEvent
        """
        
        self._schedule_experiment = schedule_experiment

    @property
    def successful_charge_card(self):
        """
        Gets the successful_charge_card of this QueueEvent.


        :return: The successful_charge_card of this QueueEvent.
        :rtype: SuccessfulChargeCardEvent
        """
        return self._successful_charge_card

    @successful_charge_card.setter
    def successful_charge_card(self, successful_charge_card):
        """
        Sets the successful_charge_card of this QueueEvent.


        :param successful_charge_card: The successful_charge_card of this QueueEvent.
        :type: SuccessfulChargeCardEvent
        """
        
        self._successful_charge_card = successful_charge_card

    @property
    def time_spent(self):
        """
        Gets the time_spent of this QueueEvent.


        :return: The time_spent of this QueueEvent.
        :rtype: TimeSpentEvent
        """
        return self._time_spent

    @time_spent.setter
    def time_spent(self, time_spent):
        """
        Sets the time_spent of this QueueEvent.


        :param time_spent: The time_spent of this QueueEvent.
        :type: TimeSpentEvent
        """
        
        self._time_spent = time_spent

    @property
    def trial_ends(self):
        """
        Gets the trial_ends of this QueueEvent.


        :return: The trial_ends of this QueueEvent.
        :rtype: TrialEndsEvent
        """
        return self._trial_ends

    @trial_ends.setter
    def trial_ends(self, trial_ends):
        """
        Sets the trial_ends of this QueueEvent.


        :param trial_ends: The trial_ends of this QueueEvent.
        :type: TrialEndsEvent
        """
        
        self._trial_ends = trial_ends

    @property
    def upload_storage_event(self):
        """
        Gets the upload_storage_event of this QueueEvent.


        :return: The upload_storage_event of this QueueEvent.
        :rtype: UploadStorageEvent
        """
        return self._upload_storage_event

    @upload_storage_event.setter
    def upload_storage_event(self, upload_storage_event):
        """
        Sets the upload_storage_event of this QueueEvent.


        :param upload_storage_event: The upload_storage_event of this QueueEvent.
        :type: UploadStorageEvent
        """
        
        self._upload_storage_event = upload_storage_event

    @property
    def user_id(self):
        """
        Gets the user_id of this QueueEvent.


        :return: The user_id of this QueueEvent.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this QueueEvent.


        :param user_id: The user_id of this QueueEvent.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def user_page_view(self):
        """
        Gets the user_page_view of this QueueEvent.


        :return: The user_page_view of this QueueEvent.
        :rtype: UserPageViewEvent
        """
        return self._user_page_view

    @user_page_view.setter
    def user_page_view(self, user_page_view):
        """
        Sets the user_page_view of this QueueEvent.


        :param user_page_view: The user_page_view of this QueueEvent.
        :type: UserPageViewEvent
        """
        
        self._user_page_view = user_page_view

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other




