def test_signature_complexity(run_validator_for_test_files):
    errors = run_validator_for_test_files(
        'test_complex_signature_tests.py',
        allowed_test_arguments_count=2,
    )
    FP004s = [error for error in errors if 'FP004' in error[2]]

    assert len(FP004s) == 1
