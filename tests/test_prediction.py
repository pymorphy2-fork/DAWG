import pytest

import dawg


class TestPrediction:
    DATA = [
        "ЁЖИК",
        "ЁЖИКЕ",
        "ЁЖ",
        "ДЕРЕВНЯ",
        "ДЕРЁВНЯ",
        "ЕМ",
        "ОЗЕРА",
        "ОЗЁРА",
        "ОЗЕРО",
    ]
    LENGTH_DATA = list(zip(DATA, ((len(w),) for w in DATA)))

    REPLACES = dawg.DAWG.compile_replaces({"Е": "Ё"})

    SUITE = [
        ("УЖ", []),
        ("ЕМ", ["ЕМ"]),
        ("ЁМ", []),
        ("ЁЖ", ["ЁЖ"]),
        ("ЕЖ", ["ЁЖ"]),
        ("ЁЖИК", ["ЁЖИК"]),
        ("ЕЖИКЕ", ["ЁЖИКЕ"]),
        ("ДЕРЕВНЯ", ["ДЕРЕВНЯ", "ДЕРЁВНЯ"]),
        ("ДЕРЁВНЯ", ["ДЕРЁВНЯ"]),
        ("ОЗЕРА", ["ОЗЕРА", "ОЗЁРА"]),
        ("ОЗЕРО", ["ОЗЕРО"]),
    ]

    SUITE_ITEMS = [(it[0], [(w, [(len(w),)]) for w in it[1]]) for it in SUITE]  # key  # item, value pair

    SUITE_VALUES = [(it[0], [[(len(w),)] for w in it[1]]) for it in SUITE]  # key

    @pytest.mark.parametrize(("word", "prediction"), SUITE)
    def test_dawg_prediction(self, word, prediction):
        d = dawg.DAWG(self.DATA)
        assert d.similar_keys(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE)
    def test_record_dawg_prediction(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_keys(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE_ITEMS)
    def test_record_dawg_items(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_items(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE_VALUES)
    def test_record_dawg_items_values(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_item_values(word, self.REPLACES) == prediction


class TestMultiValuedPrediction:
    DATA = "хлѣб ёлка ель лѣс лѣсное всё всѣ бѣлёная изобрѣтён лев лёв лѣв вѣнскій".split(" ")
    LENGTH_DATA = list(zip(DATA, ((len(w),) for w in DATA)))

    REPLACES = dawg.DAWG.compile_replaces({"е": ["ё", "ѣ"], "и": "і"})

    SUITE = [
        ("осел", []),
        ("ель", ["ель"]),
        ("ёль", []),
        ("хлеб", ["хлѣб"]),
        ("елка", ["ёлка"]),
        ("лесное", ["лѣсное"]),
        ("лесноё", []),
        ("лёсное", []),
        ("изобретен", ["изобрѣтён"]),
        ("беленая", ["бѣлёная"]),
        ("белёная", ["бѣлёная"]),
        ("бѣленая", ["бѣлёная"]),
        ("бѣлёная", ["бѣлёная"]),
        ("белѣная", []),
        ("бѣлѣная", []),
        ("все", ["всё", "всѣ"]),
        ("лев", ["лев", "лёв", "лѣв"]),
        ("венский", ["вѣнскій"]),
    ]

    SUITE_ITEMS = [(it[0], [(w, [(len(w),)]) for w in it[1]]) for it in SUITE]  # key  # item, value pair

    SUITE_VALUES = [(it[0], [[(len(w),)] for w in it[1]]) for it in SUITE]  # key

    @pytest.mark.parametrize(("word", "prediction"), SUITE)
    def test_dawg_prediction(self, word, prediction):
        d = dawg.DAWG(self.DATA)
        assert d.similar_keys(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE)
    def test_record_dawg_prediction(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_keys(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE_ITEMS)
    def test_record_dawg_items(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_items(word, self.REPLACES) == prediction

    @pytest.mark.parametrize(("word", "prediction"), SUITE_VALUES)
    def test_record_dawg_items_values(self, word, prediction):
        d = dawg.RecordDAWG("=H", self.LENGTH_DATA)
        assert d.similar_item_values(word, self.REPLACES) == prediction
