import numpy as np


def perform_first_verification():
    for n in range(20, 22):
        print(
            f"Performing the verification for quartic graphs on {n} "
            f"vertices..."
        )

        for alpha in range(1, (n + 1) // 2):
            beta = n - 1 - alpha
            print(f"\tResolving the case (alpha, beta) = ({alpha}, {beta})...")

            a1 = (
                4.0 * n - 16.0 + np.sqrt(12.0 * beta * n * (n - 13.0) / alpha)
            ) / (n - 1.0)
            b1 = (
                4.0 * n - 16.0 - np.sqrt(12.0 * alpha * n * (n - 13.0) / beta)
            ) / (n - 1.0)
            assert np.isclose(alpha * a1 + beta * b1, 4 * n - 16)
            assert np.isclose(alpha * a1 * a1 + beta * b1 * b1, 28 * n - 256)

            if (np.isclose(a1, 0) or a1 > 0) and (np.isclose(b1, 0) or b1 > 0):
                energy = alpha * np.sqrt(np.abs(a1)) + beta * np.sqrt(
                    np.abs(b1)
                )
                assert energy < 2 * n - 6
                print(
                    f"\t\tThe first solution (A, B) = ({a1:.4f}, {b1:.4f}) is "
                    f"feasible and the required sum equals {energy:.4f}, "
                    f"which is indeed below {2 * n - 6}!"
                )
            else:
                print(
                    f"\t\tThe first solution (A, B) = ({a1:.4f}, {b1:.4f}) is "
                    f"infeasible!"
                )

            a2 = (
                4.0 * n - 16.0 - np.sqrt(12.0 * beta * n * (n - 13.0) / alpha)
            ) / (n - 1.0)
            b2 = (
                4.0 * n - 16.0 + np.sqrt(12.0 * alpha * n * (n - 13.0) / beta)
            ) / (n - 1.0)
            assert np.isclose(alpha * a2 + beta * b2, 4 * n - 16)
            assert np.isclose(alpha * a2 * a2 + beta * b2 * b2, 28 * n - 256)

            if (np.isclose(a2, 0) or a2 > 0) and (np.isclose(b2, 0) or b2 > 0):
                energy = alpha * np.sqrt(np.abs(a2)) + beta * np.sqrt(
                    np.abs(b2)
                )
                assert energy < 2 * n - 6
                print(
                    f"\t\tThe second solution (A, B) = ({a2:.4f}, {b2:.4f}) "
                    f"is feasible and the required sum equals {energy:.4f}, "
                    f"which is indeed below {2 * n - 6}!"
                )
            else:
                print(
                    f"\t\tThe second solution (A, B) = ({a2:.4f}, {b2:.4f}) "
                    f"is infeasible!"
                )

        print()


def perform_second_verification():
    for n in range(20, 22):
        print(
            f"Performing the verification for subquartic graphs on {n} "
            f"vertices and {2 * n - 1} edges..."
        )

        for alpha in range(1, (n + 2) // 2):
            beta = n - alpha
            print(f"\tResolving the case (alpha, beta) = ({alpha}, {beta})...")

            a1 = (
                4.0 * n
                - 2.0
                + np.sqrt(beta * (12.0 * n * n - 14.0 * n - 4.0) / alpha)
            ) / n
            b1 = (
                4.0 * n
                - 2.0
                - np.sqrt(alpha * (12.0 * n * n - 14.0 * n - 4.0) / beta)
            ) / n
            assert np.isclose(alpha * a1 + beta * b1, 4 * n - 2)
            assert np.isclose(alpha * a1 * a1 + beta * b1 * b1, 28 * n - 30)

            if (np.isclose(a1, 0) or a1 > 0) and (np.isclose(b1, 0) or b1 > 0):
                energy = alpha * np.sqrt(np.abs(a1)) + beta * np.sqrt(
                    np.abs(b1)
                )
                assert energy < 2 * n - 2
                print(
                    f"\t\tThe first solution (A, B) = ({a1:.4f}, {b1:.4f}) is "
                    f"feasible and the required sum equals {energy:.4f}, "
                    f"which is indeed below {2 * n - 2}!"
                )
            else:
                print(
                    f"\t\tThe first solution (A, B) = ({a1:.4f}, {b1:.4f}) is "
                    f"infeasible!"
                )

            a2 = (
                4.0 * n
                - 2.0
                - np.sqrt(beta * (12.0 * n * n - 14.0 * n - 4.0) / alpha)
            ) / n
            b2 = (
                4.0 * n
                - 2.0
                + np.sqrt(alpha * (12.0 * n * n - 14.0 * n - 4.0) / beta)
            ) / n
            assert np.isclose(alpha * a2 + beta * b2, 4 * n - 2)
            assert np.isclose(alpha * a2 * a2 + beta * b2 * b2, 28 * n - 30)

            if (np.isclose(a2, 0) or a2 > 0) and (np.isclose(b2, 0) or b2 > 0):
                energy = alpha * np.sqrt(np.abs(a2)) + beta * np.sqrt(
                    np.abs(b2)
                )
                assert energy < 2 * n - 2
                print(
                    f"\t\tThe second solution (A, B) = ({a2:.4f}, {b2:.4f}) "
                    f"is feasible and the required sum equals {energy:.4f}, "
                    f"which is indeed below {2 * n - 2}!"
                )
            else:
                print(
                    f"\t\tThe second solution (A, B) = ({a2:.4f}, {b2:.4f}) "
                    f"is infeasible!"
                )

        print()


if __name__ == "__main__":
    perform_first_verification()
    perform_second_verification()
    print("All done!")
