

def post_user(api, suffix: str, number: int):
    return api.post_user(
        f'First_{suffix}_{number}',
        f'Last_{suffix}_{number}',
        f'test_{suffix}_{number}@test.test'
    )


def get_json(decorator_expected_status=200, decorator_return_value=True):
    def inner_decorator(f):
        def inner_f(*args, **kwargs):
            expected_status = kwargs.pop('expected_status', decorator_expected_status)
            return_value = kwargs.pop('return_value', decorator_return_value)
            result = f(*args, **kwargs)
            assert result.status_code == expected_status
            if return_value:
                return result.json()
        return inner_f
    return inner_decorator


def get_ids(resources):
    return sorted([resource['id'] for resource in resources])
