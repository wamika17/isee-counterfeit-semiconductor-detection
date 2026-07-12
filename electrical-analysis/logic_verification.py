
EXPECTED_TRUTH_TABLE = {
    (0, 0): 1,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0
}


def verify_logic(test_results):

    passed = 0

    total = len(test_results)

    verification = []

    for A, B, measured in test_results:

        expected = EXPECTED_TRUTH_TABLE[(A, B)]

        status = measured == expected

        if status:
            passed += 1

        verification.append({
            "Input A": A,
            "Input B": B,
            "Expected": expected,
            "Measured": measured,
            "Pass": status
        })

    accuracy = (passed / total) * 100

    return verification, accuracy


if __name__ == "__main__":

    sample_results = [

        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)

    ]

    report, accuracy = verify_logic(sample_results)

    print(report)

    print(f"\nTruth Table Accuracy: {accuracy:.2f}%")
