
def register_routes(api, app, root="api"):
    # from app.widget import register_routes as attach_widget
    # from app.fizz import register_routes as attach_fizz
    # from app.other_api import register_routes as attach_other_api
    # from app.third_party.app import create_bp

    # # Add routes
    # attach_widget(api, app)
    # attach_fizz(api, app)
    # attach_other_api(api, app)
    # from app.controllers.test import api as test_api

    # api.add_namespace(test_api, path='/test')
    from app.doctor import register_routes as attach_doctor
    from app.patient import register_routes as attach_patient

    attach_doctor(api, app)
    attach_patient(api, app)
