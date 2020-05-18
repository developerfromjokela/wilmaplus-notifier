#  Copyright (c) 2020 openKirkes, developed by Developer From Jokela


class RequestResult:

    def __init__(self, error, exception=None, response=None):
        self.error = error
        self.exception = exception
        self.response = response
        if error and exception is None:
            raise Exception("Exception cannot be None when error is True")

    def get_exception(self):
        return self.exception

    def is_error(self):
        return self.error

    def get_response(self):
        return self.response


class ErrorResult(RequestResult):

    def __init__(self, exception):
        super().__init__(True, exception)


class LoginResult(RequestResult):

    def __init__(self, session):
        super().__init__(False, None, None)
        self.session = session

    def get_session(self):
        return self.session


class SessionValidateResult(RequestResult):

    def __init__(self, validation, user_id, user_type):
        super().__init__(False, None, None)
        self.validation = validation
        self.user_id = user_id
        self.user_type = user_type

    def get_combined_user_id(self):
        return str(self.user_id) + "_" + str(self.user_type)

    def is_valid_session(self):
        return self.validation


class PushSendRequest(RequestResult):

    def __init__(self, success):
        super().__init__(False, None, None)
        self.success = success

    def is_sent(self):
        return self.success


class PushDetailsRequest(RequestResult):

    def __init__(self, details):
        super().__init__(False, None, None)
        self.details = details

    def get_details(self):
        return self.details


class ExamsResult(RequestResult):

    def __init__(self, exams):
        super().__init__(False, None, None)
        self.exams = exams

    def get_exams(self):
        return self.exams


class ObservationsResult(RequestResult):

    def __init__(self, observations):
        super().__init__(False, None, None)
        self.observations = observations

    def get_observations(self):
        return self.observations


class NewsResult(RequestResult):

    def __init__(self, news):
        super().__init__(False, None, None)
        self.news = news

    def get_news(self):
        return self.news
