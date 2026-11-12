"""Kiểm tra nhanh hai thuật toán trên basket demo.

Chạy từ repo gốc:
    python tests/smoke_test.py
Không cần Jupyter, không tải dữ liệu ngoài mạng.
"""
from pathlib import Path

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "data" / "basket_demo.csv"
SUPPORTS = (0.10, 0.20)
MAX_LEN = 3
MIN_CONFIDENCE = 0.30


def rules_for(itemsets: pd.DataFrame) -> pd.DataFrame:
    if itemsets.empty or not itemsets["itemsets"].map(len).ge(2).any():
        return pd.DataFrame()
    return association_rules(
        itemsets, metric="confidence", min_threshold=MIN_CONFIDENCE
    )


def itemsets_dict(dataframe: pd.DataFrame) -> dict:
    return {
        tuple(sorted(items)): float(support)
        for support, items in zip(dataframe["support"], dataframe["itemsets"])
    }


def rules_dict(dataframe: pd.DataFrame) -> dict:
    if dataframe.empty:
        return {}
    return {
        (tuple(sorted(a)), tuple(sorted(b))): (float(s), float(c), float(l))
        for a, b, s, c, l in zip(
            dataframe["antecedents"],
            dataframe["consequents"],
            dataframe["support"],
            dataframe["confidence"],
            dataframe["lift"],
        )
    }


def assert_equal_float_maps(a: dict, b: dict) -> None:
    assert a.keys() == b.keys(), "Khác tập mục hoặc luật."
    for key in a:
        x, y = a[key], b[key]
        if isinstance(x, tuple):
            assert all(abs(i - j) < 1e-9 for i, j in zip(x, y)), key
        else:
            assert abs(x - y) < 1e-9, key


def main() -> None:
    basket = pd.read_csv(FILE, index_col=0)
    assert basket.shape == (40, 9), basket.shape
    assert basket.isin((0, 1)).all().all()
    basket = basket.astype(bool)

    for support in SUPPORTS:
        apr = apriori(
            basket, min_support=support, max_len=MAX_LEN, use_colnames=True
        )
        fp = fpgrowth(
            basket, min_support=support, max_len=MAX_LEN, use_colnames=True
        )
        apr_rules = rules_for(apr)
        fp_rules = rules_for(fp)

        assert_equal_float_maps(itemsets_dict(apr), itemsets_dict(fp))
        assert_equal_float_maps(rules_dict(apr_rules), rules_dict(fp_rules))
        assert len(fp_rules) >= 5, "Demo cần ít nhất 5 luật để sinh viên làm bài."
        print(
            f"PASS min_support={support:.2f}: "
            f"{len(fp)} itemsets, {len(fp_rules)} rules"
        )

    print("PASS: Apriori/FP-Growth trả về cùng tập mục, support và luật.")


if __name__ == "__main__":
    main()
