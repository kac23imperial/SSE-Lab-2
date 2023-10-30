from app import process_query


def test_knows_about_dinosaurs():
    assert (
            process_query("dinosaurs") ==
            "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def asking_for_name():
    assert process_query("What is your name?") == "Karen and Nicole"


def test_largest_number():
    assert process_query("Which of the following numbers is the largest:"
                         " 61, 34, 2?") == "61"


def test_multiplying():
    assert process_query("What is 5 multiplied by 3?") == "15"


def test_addition():
    assert process_query("What is 5 plus 3?") == "8"
