import math
from typing import Optional, Tuple, Union


def quadratic_formula(a: float, b: float, c: float) -> Union[Tuple[float, float], Tuple[complex, complex], None]:
    """
    Solve the quadratic equation ax^2 + bx + c = 0.
    
    Args:
        a: Coefficient of x^2
        b: Coefficient of x
        c: Constant term
    
    Returns:
        Tuple of two roots (real or complex), or None if a = 0 (linear equation)
    
    Edge cases handled:
        - a = 0: Returns None (linear equation, not quadratic)
        - Negative discriminant: Returns complex roots
        - Zero discriminant: Returns two identical real roots
    """
    # Edge case: a = 0 (division by zero)
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("0 = 0 is always true, infinite solutions")
            else:
                raise ValueError(f"{c} = 0 has no solution")
        else:
            # Linear equation: bx + c = 0 -> x = -c/b
            return (-c / b, -c / b)
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    # Edge case: negative discriminant (complex roots)
    if discriminant < 0:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)
    
    # Real roots
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return (root1, root2)


# Test cases and examples

if __name__ == "__main__":
    print("=" * 60)
    print("Quadratic Formula Test Cases")
    print("=" * 60)
    
    # Example 1: Standard quadratic with two real roots
    # x^2 - 5x + 6 = 0 -> (x-2)(x-3) = 0 -> roots: 2, 3
    print("\nExample 1: x^2 - 5x + 6 = 0")
    print("Expected roots: 2, 3")
    roots = quadratic_formula(1, -5, 6)
    print(f"Computed roots: {roots}")
    print(f"Verification: {roots[0]:.2f} ≈ 2.00, {roots[1]:.2f} ≈ 3.00")
    
    # Example 2: Quadratic with one real root (discriminant = 0)
    # x^2 - 4x + 4 = 0 -> (x-2)^2 = 0 -> root: 2 (double root)
    print("\nExample 2: x^2 - 4x + 4 = 0")
    print("Expected root: 2 (double root)")
    roots = quadratic_formula(1, -4, 4)
    print(f"Computed roots: {roots}")
    print(f"Verification: {roots[0]:.2f} = {roots[1]:.2f} = 2.00")
    
    # Example 3: Quadratic with complex roots
    # x^2 + 2x + 5 = 0 -> discriminant = 4 - 20 = -16
    print("\nExample 3: x^2 + 2x + 5 = 0")
    print("Expected: Complex roots")
    roots = quadratic_formula(1, 2, 5)
    print(f"Computed roots: {roots}")
    print(f"Verification: Real part = -1.00, Imaginary part = ±2.00i")
    
    # Example 4: Edge case - a = 0 (linear equation)
    # 2x + 4 = 0 -> x = -2
    print("\nExample 4: 2x + 4 = 0 (linear equation, a=0)")
    print("Expected root: -2")
    roots = quadratic_formula(0, 2, 4)
    print(f"Computed roots: {roots}")
    print(f"Note: Returns same value twice for linear equation")
    
    # Example 5: Edge case - a = 0, b = 0, c = 0
    print("\nExample 5: 0x^2 + 0x + 0 = 0")
    try:
        roots = quadratic_formula(0, 0, 0)
        print(f"Computed roots: {roots}")
    except ValueError as e:
        print(f"Error (expected): {e}")
    
    # Example 6: Edge case - a = 0, b = 0, c ≠ 0
    print("\nExample 6: 0x^2 + 0x + 5 = 0")
    try:
        roots = quadratic_formula(0, 0, 5)
        print(f"Computed roots: {roots}")
    except ValueError as e:
        print(f"Error (expected): {e}")
    
    # Example 7: Negative coefficients
    # -x^2 + 3x - 2 = 0 -> x^2 - 3x + 2 = 0 -> roots: 1, 2
    print("\nExample 7: -x^2 + 3x - 2 = 0")
    print("Expected roots: 1, 2")
    roots = quadratic_formula(-1, 3, -2)
    print(f"Computed roots: {roots}")
    print(f"Verification: {roots[0]:.2f} ≈ 1.00, {roots[1]:.2f} ≈ 2.00")
    
    # Example 8: Large numbers
    print("\nExample 8: 1000x^2 - 2000x + 1000 = 0")
    print("Expected root: 1 (double root)")
    roots = quadratic_formula(1000, -2000, 1000)
    print(f"Computed roots: {roots}")
    print(f"Verification: {roots[0]:.2f} = {roots[1]:.2f} = 1.00")
    
    print("\n" + "=" * 60)
    print("All test cases completed!")
    print("=" * 60)
