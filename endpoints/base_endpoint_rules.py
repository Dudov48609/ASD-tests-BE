import allure


class EndpointMainRules:
    status_code = None

    def is_response_200(self):
        with allure.step('Checking response status'):
            return self.status_code == 200
