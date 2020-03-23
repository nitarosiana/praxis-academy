from injector import Module, singleton, Injector, provider
class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result

class AppModule(Module):
    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        return Api()


class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api called')
        return 24


class TestAppModule(Module):
    @singleton
    @provider
    def provide_api(self) -> Api:
        return TestApi()


if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()