import pytest
from hypothesis import given, strategies as st
from src.tasks import generate_unique_id

@given(st.lists(st.dictionaries(keys=st.just("id"), values=st.integers(min_value=0, max_value=1000))))
def test_generate_unique_id_property(tasks):
    unique_id = generate_unique_id(tasks)
    ids = [task["id"] for task in tasks]
    assert unique_id > max(ids, default=0)
