import pytest
from slist import SList
from course import Course


def test_insert():
    slist = SList()
    assert repr(slist) == '[]'
    slist.insert(value= Course(number=2))
    slist.insert(value=Course(number=3))
    assert repr(slist) == '[2, 3]'
    slist.insert(value=Course(number= 4))
    assert repr(slist) == '[2, 3, 4]'
    slist.insert(value=Course(number= 5))
    assert repr(slist) == '[2, 3, 4, 5]'
    slist.insert(value=Course(number= 1))
    assert repr(slist) == '[1, 2, 3, 4, 5]'
    assert slist.size() == 5

def test_find():
    slist = SList()
    new_course = Course(number= 10)
    slist.insert(value=Course(number= 2))
    slist.insert(value=Course(number= 3))
    slist.insert(value=Course(number= 4))
    slist.insert(value=Course(number= 5))
    slist.insert(value=Course(number= 5))
    slist.insert(value=Course(number= 1))
    slist.insert(value=new_course)
    assert repr(slist) == '[1, 2, 3, 4, 5, 5, 10]'
    assert len(slist) == 7
    assert slist.find(new_course) == new_course

def test_remove():
    slist = SList()
    new_course = Course(number= 10)
    other_course = Course(number= 5)
    slist.insert(value=Course(number= 2))
    slist.insert(value=Course(number= 3))
    slist.insert(value=Course(number= 4))
    slist.insert(value=other_course)
    slist.insert(value=other_course)
    slist.insert(value=Course(number= 1))
    slist.insert(value=new_course)
    assert repr(slist) == '[1, 2, 3, 4, 5, 5, 10]'
    assert len(slist) == 7
    assert slist.remove(other_course) == True
    assert repr(slist) == '[1, 2, 3, 4, 5, 10]'
    assert len(slist) == 6



def test_remove_all():
    slist = SList()
    new_course = Course(number= 5)
    slist.insert(value=Course(number= 2))
    slist.insert(value=Course(number= 3))
    slist.insert(value=Course(number= 4))
    slist.insert(value=new_course)
    slist.insert(value=new_course)
    slist.insert(value=Course(number= 1))
    assert repr(slist) == '[1, 2, 3, 4, 5, 5]'
    slist.remove_all(new_course)
    assert repr(slist) == '[1, 2, 3, 4]'

def test_size():
    slist = SList()
    slist.insert(value=0)
    slist.insert(value=1)
    slist.insert(value=-1)
    slist.insert(value=12)
    slist.insert(value=5)
    slist.insert(value=6)
    slist.insert(value=5)
    assert slist.size() == 7
    slist.remove(5)
    assert slist.size() == 6
    slist.remove(15)
    assert slist.size() == 6

def test_get_item():
    slist = SList()
    slist.insert(value=0)
    slist.insert(value=1)
    slist.insert(value=-1)
    slist.insert(value=12)
    slist.insert(value=5)
    slist.insert(value=6)
    slist.insert(value=5)
    assert slist[0].value == -1
    with pytest.raises(IndexError):
        slist[7]
    assert slist[-1].value == 12
    assert slist[-2].value == 6