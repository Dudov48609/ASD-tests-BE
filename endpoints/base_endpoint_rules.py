

class EndpointMainRules:
    status_code = None

    def is_response_200(self):
        return self.status_code == 200
