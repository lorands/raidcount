# Raidcount Quick Start

Score your first kabaddi match in two minutes.

## 1. Install

```shell
pip install raidcount
```

## 2. Start a match

```shell
raidcount new "Bengal Warriors" "Puneri Paltan"
```

## 3. Score each raid

```shell
raidcount raid --team A --touch 2 --bonus
raidcount raid --team B --touch 1
```

A raid earns a point for each defender touched and one for the bonus line.
A tackled raider gives the defending team a point.

## 4. Check the score

```shell
raidcount score
Bengal Warriors 3 : 1 Puneri Paltan
```
