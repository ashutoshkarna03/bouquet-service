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
