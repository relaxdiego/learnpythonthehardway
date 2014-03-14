from nose.tools import *
from ex48 import parser

def assert_sentence_equal(expected, actual):
    assert_is_not_none(actual)
    assert_equal(expected.subject, actual.subject)
    assert_equal(expected.verb, actual.verb)
    assert_equal(expected.object, actual.object)


def test_sentence():
    subj = ('noun', 'bear')
    verb = ('verb', 'kill')
    obj = ('noun', 'skunk')

    sentence = parser.Sentence(subj, verb, obj)

    assert_equal(sentence.subject, subj[1])
    assert_equal(sentence.verb, verb[1])
    assert_equal(sentence.object, obj[1])


def test_peek():
    # Test for when there's one token
    word_type = parser.peek([('noun', 'bear')])
    assert_is_not_none(word_type)
    assert_equal('noun', word_type)

    # Test for when there are multiple tokens
    word_type = parser.peek([('noun', 'bear'), ('stop', 'the')])
    assert_is_not_none(word_type)
    assert_equal('noun', word_type)

    # Test for when there are no tokens
    word_type = parser.peek([])
    assert_is_none(word_type)


def test_match():
    word_list = [('verb', 'kill'),
                 ('stop', 'the'),
                 ('noun', 'bear')]

    # When there's a match
    word = parser.match(word_list[:], 'verb')
    assert_equal('verb', word[0])

    # When there's no match
    word = parser.match(word_list[:], 'stop')
    assert_is_none(word)

    # When word_list is null
    word = parser.match(None, 'stop')
    assert_is_none(word)


def test_skip():
    word_list = [('verb', 'kill'),
                 ('stop', 'the'),
                 ('noun', 'bear')]

    word = parser.skip(word_list, 'verb')
    assert_equal(2, len(word_list))
    assert_equal([('stop', 'the'), ('noun', 'bear')], word_list)


def test_parse_verb():
    word_list = [('verb', 'kill'),
                 ('stop', 'the'),
                 ('noun', 'bear')]

    word = parser.parse_verb(word_list)
    assert_equal(('verb', 'kill'), word)

    assert_raises(parser.ParserError, parser.parse_verb, word_list)


def test_parse_object():
    # When object is a noun
    word_list = [('stop', 'the'), ('noun', 'bear')]
    word = parser.parse_object(word_list)
    assert_equal(('noun', 'bear'), word)

    # When object is a direction
    word_list = [('stop', 'the'), ('direction', 'north')]
    word = parser.parse_object(word_list)
    assert_equal(('direction', 'north'), word)

    # When object is neither a noun or direction
    word_list = [('stop', 'the'), ('verb', 'stop')]
    assert_raises(parser.ParserError, parser.parse_object, word_list)


def test_parse_subject():
    subject = 'something'
    verb = ('verb', 'kill')
    obj = ('noun', 'bear')
    word_list = [verb, ('stop', 'the'), obj]

    actual = parser.parse_subject(word_list, subject)
    expect = parser.Sentence(subject, verb, obj)

    assert_sentence_equal(expect, actual)


def test_parse_sentence():
    player = ('noun', 'player')
    bear = ('noun', 'bear')
    verb = ('verb', 'go')
    direction = ('direction', 'north')

    # When subject is not the player
    word_list = [bear, verb, direction]
    expect = parser.Sentence(bear, verb, direction)
    actual = parser.parse_sentence(word_list)
    assert_sentence_equal(expect, actual)
    
    # When subject is the player
    word_list = [verb, direction]
    expect = parser.Sentence(player, verb, direction)
    actual = parser.parse_sentence(word_list)    
    assert_sentence_equal(expect, actual)

    # When subject is invalid
    word_list = [('stop', 'the'), ('error', 'whatever')]
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)
