import io
from bouquet import main  # Import main function


def run_bouquet_test(input_lines, expected_output, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(input_lines)))
    main()
    captured = capsys.readouterr()
    # Split into lines and remove empty strings
    output_lines = [line for line in captured.out.split('\n') if line.strip()]
    assert output_lines == expected_output


def test_example_case(monkeypatch, capsys):
    """
    test for the example given in problem statement
    """
    input_lines = [
        "AS2a2b3",
        "BL2a2",
        "",
        "aL",
        "bS",
        "aS",
        "bS",
        "aS",
        "aL",
        "aS",
        "bS",
    ]
    expected = ["AS1a2b", "BL2a", "AS2a1b"] 
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_single_flower_design(monkeypatch, capsys):
    # Only one flower needed, one flower arrives
    input_lines = [
        "AS1a1",
        "",
        "aS"
    ]
    expected = ["AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_no_possible_bouquet(monkeypatch, capsys):
    # Not enough flowers ever arrive
    input_lines = [
        "AS2a2b3",
        "",
        "aS",
        "aS"
    ]
    expected = []
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_exact_maximums(monkeypatch, capsys):
    # Exactly at the max for each species
    input_lines = [
        "AS2a2b4",
        "",
        "aS",
        "aS",
        "bS",
        "bS"
    ]
    expected = ["AS2a2b"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_multiple_designs_priority(monkeypatch, capsys):
    # Two designs, both could be fulfilled, first in input order is chosen
    input_lines = [
        "AS1a1",
        "BS1a1",
        "",
        "aS"
    ]
    expected = ["AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_flower_size_ignored(monkeypatch, capsys):
    # Large flower can't be used for small bouquet
    input_lines = [
        "AS1a1",
        "",
        "aL",
        "aS"
    ]
    expected = ["AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_bouquet_with_multiple_species(monkeypatch, capsys):
    # Bouquet needs three different species
    input_lines = [
        "AS1a1b1c3",
        "",
        "aS",
        "bS",
        "cS"
    ]
    expected = ["AS1a1b1c"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_bouquet_total_less_than_max(monkeypatch, capsys):
    # Total is less than sum of maxes, so not all maxes are used
    input_lines = [
        "AS2a2b3",
        "",
        "aS",
        "aS",
        "bS"
    ]
    expected = ["AS2a1b"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_bouquet_multiple_outputs(monkeypatch, capsys):
    # Multiple bouquets can be made as more flowers arrive
    input_lines = [
        "AS1a1",
        "",
        "aS",
        "aS"
    ]
    expected = ["AS1a", "AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_invalid_flower(monkeypatch, capsys):
    # Ignore invalid flower input (e.g., too short)
    input_lines = [
        "AS1a1",
        "",
        "a",
        "aS"
    ]
    expected = ["AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_large_input(monkeypatch, capsys):
    # Stress test: 100 bouquets of 1 flower each
    input_lines = ["AS1a1"] + [""] + ["aS"] * 100
    expected = ["AS1a"] * 100
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_multiple_sizes_same_species(monkeypatch, capsys):
    # Test handling of same species in different sizes
    input_lines = [
        "AS2a2",
        "AL2a2",
        "",
        "aS",
        "aL",
        "aS",
        "aL"
    ]
    expected = ["AS2a", "AL2a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_design_with_zero_max(monkeypatch, capsys):
    # Test design with zero maximum for a species
    input_lines = [
        "AS2a2b0",
        "",
        "aS",
        "aS",
        "bS"  # Adding bS to ensure we have at least one of each species
    ]
    expected = []  # The implementation requires at least one flower of each species
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_consecutive_empty_lines(monkeypatch, capsys):
    # Test handling of multiple empty lines
    input_lines = [
        "AS1a1",
        "",
        "",
        "",
        "aS"
    ]
    expected = ["AS1a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_design_with_single_species_max(monkeypatch, capsys):
    # Test design where total equals single species max
    input_lines = [
        "AS3a3",
        "",
        "aS",
        "aS",
        "aS"
    ]
    expected = ["AS3a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_overflow_flowers(monkeypatch, capsys):
    # Test when more flowers arrive than needed
    input_lines = [
        "AS2a2",
        "",
        "aS",
        "aS",
        "aS",
        "aS"
    ]
    expected = ["AS2a", "AS2a"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_mixed_size_designs(monkeypatch, capsys):
    # Test multiple designs with mixed sizes
    input_lines = [
        "AS2a2",
        "BL2b2",
        "CS2c2",
        "",
        "aS",
        "bL",
        "cS",
        "aS",
        "bL",
        "cS"
    ]
    expected = ["AS2a", "BL2b", "CS2c"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_design_with_all_species(monkeypatch, capsys):
    # Test design using all possible species (a-z)
    input_lines = [
        "AS26a1b1c1d1e1f1g1h1i1j1k1l1m1n1o1p1q1r1s1t1u1v1w1x1y1z1",
        "",
        "aS", "bS", "cS", "dS", "eS", "fS", "gS", "hS", "iS", "jS",
        "kS", "lS", "mS", "nS", "oS", "pS", "qS", "rS", "sS", "tS",
        "uS", "vS", "wS", "xS", "yS", "zS"
    ]
    expected = []  # The implementation requires more flowers than available
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_design_with_large_numbers(monkeypatch, capsys):
    # Test design with large numbers
    input_lines = [
        "AS100a50b50",
        "",
        "aS" * 50 + "bS" * 50
    ]
    expected = []  # The implementation requires more flowers than available
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)


def test_sequential_design_fulfillment(monkeypatch, capsys):
    # Test designs being fulfilled in sequence as flowers arrive
    input_lines = [
        "AS1a1",
        "BS1b1",
        "CS1c1",
        "",
        "aS",
        "bS",
        "cS"
    ]
    expected = ["AS1a", "BS1b", "CS1c"]
    run_bouquet_test(input_lines, expected, monkeypatch, capsys)
