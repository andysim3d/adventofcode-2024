def helper(inputs):
    # convert input to 2d-array
    result = []
    for line in inputs.split():
        result.append(list(line))
    return result 

def part_1(inputs):
    grids = helper(inputs)
    row, col = len(grids), len(grids[0])
    result = 0
    eight_directions = (
        (1, 0), #down
        (-1,0), #up
        (0, 1), #right
        (0,-1), #left
        (1, 1), #right top
        (-1,1), #left top
        (1,-1), #right bottom
        (-1,-1), #left bottom
    )

    # print(dfs(0, 2, 1, 1, 0, set(), grids))
    for x in range(0, col):
        for y in range(0, row):
            for dy, dx in eight_directions:
                if dfs(y, x, dy, dx, 0, set(), grids):
                    result+= 1
    print(result)
def part_2(inputs):
    grids = helper(inputs)
    row, col = len(grids), len(grids[0])
    result = 0
    for x in range(1, col-1):
        for y in range(1, row-1):
            if grids[y][x] == "A" and find_X(y, x, grids):
                result += 1
    print(result)

def find_X(row, col, grids):
    complete = (("M","S"), ("S", "M"))
    return (grids[row-1][col-1], grids[row+1][col+1]) in complete and (grids[row+1][col-1], grids[row-1][col+1]) in complete
def dfs(row, col, drow, dcol, index, visited, grids):
    # dfs search to find XMAS
    if index >= len("XMAS"):
        # already find, stop
        return True
    if row >= len(grids) or row < 0 or col >= len(grids[0]) or col < 0:
        return False

    next_char = "XMAS"[index]
    if grids[row][col] != next_char:
        return False
    # eight_directions = (
    #     (1, 0), #down
    #     (-1,0), #up
    #     (0, 1), #right
    #     (0,-1), #left
    #     (1, 1), #right top
    #     (-1,1), #left top
    #     (1,-1), #right bottom
    #     (-1,-1), #left bottom
    # )
    result = False
    # for drow, dcol in eight_directions:
    new_row, new_col = row + drow, col + dcol
    # already visited
    if ((new_row, new_col)) in visited:
        return False
    # search out of boundry
    visited.add((new_row,new_col))
    result = result or dfs(new_row, new_col, drow, dcol, index+ 1, visited, grids)
    # visited.remove((new_row, new_col))
    return result

inputs = """MMMMASXMMMMXXMASMMXSAMMMSAMXSXMMXMXMXAMAMXSXXXMXAXAMXMMXAASAMXMSMMMSXSAMXMASAXXAMXAMXAXSXXMASXMMXMASXMAXXMASMMMMXMXSMSSSXSASASMSAMXXSMSMSSXS
MAAXMXMAAAMSMSXSXSMSAXSXSXSASAXAASAMXXSMXXMASMMSMSXSAMSMSSSMSMMAAMASMMAAMAMXMASXMSAMXSMSAAMASMXSASAMAMAMXSAMAAXMASAMASAMXSASASASXMAMSAAAXAAX
MSSSMMSSMMSAASAMAXAMAMSAMAMASAMSMSMSMMAAMSAMXAXAAAAXXXAAXAXXAXSSSMXSASXMSXXASXXAXXAXXMAMXXMASAXSASXSAMAMAMXSSMMSASAMXMMMMMAMAMAMMXSAMMMSMMSM
XMAMAAXXMMSMSMAMAMSMMMMAMXMXMAMMASASASAMMXAAMMAMSMSMMSMXMMMMMMXAMXXSAMXAAMSMXMMMMSMMSMAMXMMMMAMMXMASXSAMXMAAAXAMMMAMMXXAAMAMAMSMSAMXSXXMASXM
MMAMSXSAMAMXXXSMSMMAXSXSMASMXAMMAMAMMSASXXMMSSMXAAMXAAXMSXMAXXMASMXMAMMMMAAMAAAAXXAAMMAMSXXMMASMASMMXSXSAMXXSMSSSSMMAXSXSSMSMSAAMXSAXMAMSAMS
XSXMAXSAMASXMAXAXASMMSAAMAMXSMSMSMMMAXMMMXAAAXXMMAMMSMSASAMSAXXMMMMSAMAAXSXXMMXSMMMMSMSASAMXSASXMXAMAMASXMSXMAMXAAXSSMMAAXAMXSMSMMMMSMXMAMAX
MMAMMXMXSMSAMMMMMMMAAMSMMSSMXMAMXAAMXXXMAXMMXMXAXXXXAAXMXAMMMMXMXXASASMSXMMMSMMAMXSAMAMMXMAXMASMMSSMMMASASMSMAMMSMMMAAMMMSXMMXXAAAAMXAAMMXMS
ASXMXXMASXMAAAAAAXXMXMMXMAAAMSAMXMMMSAMXSMMASMMSSSMSMSMXSSMSASMAMXXSAMAXMASAAASMMAMAMXMMAASAMXMMMAAAXMAMMXAASAXXAAASMMMXAMASXSSMSMSSMXASAAMA
MXMXXAMXMASXMSSSSSMXAAXAMMMSMSASXAAAMSMAMMMAAMAMMAAAAAXXXAAXASAAMXAXAMAMXAMMSMMAMXSAMMMSSSMXXSXXMSSMMMSSMMSMSMSSXSMSMMMMMSAMAAXXAAXAXXAMXSSS
SMASMXMXMXMSAMXAAMMSMXSAXXXMASAMMSMSAMXAMXMXXMAMMMMMSSSMMMXMXMXAXXMSMMXSMXSXMXSMMMAMXMMAMAXMAMSMXMAAXMMAMAMMXMAXXMAXXAAAASAMXMMSMXSAMMXMXMAM
AASAMASXMAAXXSMXMAAMMMXAXSXMAMAMAXAXMASXSASXMSMSAAXMXMAASAASMSSSMAMAXMXXXMMXMMMAAMASMAMASMXXAMAMAXMMMMXAMAMXSMAXXMAMSSSSXSXMXSMXSAMXMMSMSMAM
XSMASXMASMXMMXMASMASXSXSMSAMXSMMSMMMXMMASMSAAAAMMMMMAMSMMASMAAAAXAXMXMAMXXSAMXXSASMSAXSAXXSSMSSSMSMAAMXMMSSMMMSSXMXMXAAMAMXMXMMASMSMMASMMMAX
XMAMXASXMSMAAASAAMAAMMAMMXMMAXMAAASXSAMXMAMMMMSMMXMMAMASAXXMMMMMSSMSMSAAMASMSAMXASMSXXMMSMAAAAAXAAMSMSAAXAAASAASAMXMMMMMMXAMAAMAMXXAMAMXXSAS
XMAMXMSXAAMMSXMAXMMSSMXMAAASMSMMSMMAMXSXMMSSMAXAMAMSMSAXXSXXXSAMXMAAXSAMSAMXAASMXMASAMAAAXMMMXSSSXXMASMSMSSMMMSMXMAXAMXAASMSSSMSSSMMMSSMAMSM
XSASXAXMSMSAXMSSMXAMAMMMMXXAASMMMAMSMAMAXXAAMASAMMMAMMASXMXMAAAMAMMMMMAXMASASMMMMMMMASXSXMXAXMMXXXAMXMAXXXAMSMMMAMSMSAMXXXAAAAAMAXASAMXMAXAM
MSASMMMMMAMAXXAAAXAMAMAMASMMMMAASAMXMASAMMSSMXSMMSMMSMAMAAMMSMSMAXXMMMAMSAMXMAXAAMXMAMMMASXSMMMASMMMAMXMXXMMAAASXSMAMASMXMMMSMMMAMMMMSXXSSMS
XMAMXMAAMSMSMMSSMMMSSSSMAXXMASMMSXMASXSASXAXAXMXAXASAMXSMXMAMMAXSXSASXMXAMXMASMSSMXMMMAMAMAAAXMAMSAMXMMSXASXSXMMXAMXMAMMASAMXMXMMSXAMSAMXAXA
SMXMASMSSMAMXXAXAXXAAAMMMMASASMMMMSMSMMMXMMSXMMMMXMMMMMMMAMMSAMAMAAAXAMSAMXSAMAAAASMSSXMAMXSMMMXSASAXMASXMMAMSSSSMMMMXMAMXMAXMXSAMMMXMAMSAMM
XAASASAMXMAMXMASXMMMSMMAMSXMASMAMAAMMAAXMAMSXXSAMASAMAMASXSAXMXMMXMXMXMAASXMASMMMMMAAAXSASXXAXASAAMXSMMSAXMSMAXMAXASMSXSAMXXMAAMASXMXSSMSMMX
MSMAAMXMXSMSAMAMMMSAAXMAXMASXMMAMMMMSXMMSXXMAASAXAXAMAXXSXMASXSXMSSMMASMSMMSAMXSXMXMMMMSASMSXMMXMXMAMXASXMMMMXMSAMXAAAAXSMASXMMMMMMMXMAXSASX
AAXMXMMSAMASXSASAAMSSSSSMSASASXXXAXXMSSXMXAMXMSAMSSMSSXMMAMXMAMSAAAASASXMXXSAMASAAXXXSAMXMMXMXSXMAMASMXSMMMAMAAXSMMMMMXMAMASAAMSMAAXSAMXSAMS
SSSXASAAAMMMMMAMMMXMXAAXAXXMAMASXSMASAMAASXSAXMAMXAXAAASMSMMMMMMMMSMMXSAMMAXAMASAMMMMMAXMMMXAASASXSASAMXMAAAMMSMMMAXXXAXMMASMMMASMSMMAXXMAMX
XAAMAMMXMMAASMSMXMXXMMSMMMSMMMMMAASMMASXMAMSMSSXMSXMXSMMAAMAASXSSMXXSASAMXSSMMASAMAAMMMMSASMSMSAMMMXSMMXSMSSSMAAASXSASASXMMSASXMSXMASAMMSSMM
SMMMXSMMSXSAMXXAASASAMXAMAMXAAAMXMMXSAMXMAXXMAXMXSMMMMAXMMMSXSXAAASAMXSMMMXAMMAXAMXMXSSMXAXAAXMAMASMMASXMAXXAMSSMSXSAMSAMXXSAMMXSASAMMSMAAMM
XAXXXMXAXAXMASMSMSASMXSMMSSSSSXXAXXAMASMSMSASMXSAMAAASMMMSXMAMXXMMMAMXMAMASAMXSSSMXSAMAAMSMSMMXAMSMAXAMAMAMXAMXMAXAMXMXXMMXMMMSAMAMASASMMMMM
SMMXXMAXMMMSXSXAXMAMMMSAMXAAXMASMSMMSAMXAAXAMXMMASXMXSAAXSAMXMASXXSMMAMASMSXAXMAMXAMASMMMAAAASMMMASXMSSSMMSMSMAMXMXMMSMMMXXAMAMXSAMXMAXAMAXX
SMASXMSXSAMXAMMMSAMXSAMAMMMMMMMAXMAMMMMMMXMXMXASMMXSMMMMXSAMXMXSXAMASASMSASMSMMXMMXXMMMXXMMMXMAMSAMMXMAMXAMXAMMXSAASAMAAASMSMASASAMAMXMSMMSA
XMASAAXXSMSMXMAMAMSAMXSAMXMASAMMSSSMAAMSASMSSMXSASMSXMAXXXASXMXSMXMMSASAMAMAAASXMMMMSAMMXSAMXSAMMSMMSMAMSAMSMMSAMSMSASMMMSAAMAMXSAMSMSAXAAXM
SMXSMMMXMSAMXSXMAXMASASMSMAAXAXSAMAXMMMXAMAAAXASMMAMMSMSSSXMASAXAASXMAMMMXMXMSMAAXAASAXSASAXAMAXAMXAMMAXMAMXMAMXMXXSXMXXXMMSMSSXMXMAAMASMMMM
MMMMAMMAMMXSXXXSSXSAMASAAMMASMMMASMSXSAMXMMXMMAMXMAMMAAAXMASXMXMXAMAMXMASMSMMAXMMMMXMMXMASMMSXSMSMMSSSSXSMMSMSSMMSMSMMSXXMAXAMAMSMSMSMMMMAAM
MAAMAASXMSAMAXMXAAMASAMMMSSXMAASXMXXAAXMXSMASAXXSSSSSMMMXMMMXMXMSSSMMXMASAAASAMMXMMMMMAMMMXAXAMAXXAMXMMASXAXSAAAXAXMAMAAMXMMSMSAMXMXXXXASMMM
SSSSSXXAAMXMAMAMAMSXMAMXMAXAXMMMSMXMXMMAXAMXXAMXMAAMMXSAASAMASXAAAAMMSMAXXXMMAXSASAAASASASMXSXMAMMMSAXMAMMMMMSSMMMXSSMXXMAXAXXAMSMSMMXSXMMSS
XAAAXAMXMSSSSSSSMXSMSMMAMMSSMMSMMXAMXMXXMMSSMASAMMMMXAXSASASAXMMMSMMMAMMMSMMMXMSAXMSMMASASAASMMXMXASMMMSSXSAMXXXAXAMXMAASXMMSMMXSAAAMXMAXAAA
MMMMMXAMAMXAAMASMAMMAASXSAAXAMXAAXXSSSMSMXAXMAXAXMXSMSXMXSAMMXSAAAMASMXSAAXSXXXXSMXXAMMMMMMMXASMSMMSAXXMAAMXMXMAMAAXAXSXMAMXAAXAMSSSMAXSMMSS
SSSMSMSSSMMMMMAMMASMMMMAMMSSMMSMMSXAASAAXMASMSSMSSMMAXXMAMAMXASMSXSXSAAMSSMMAMMAXMXMAMXAXXXMSAMAMSXSAMXMMMMSXMMSAXSMMMXAXMASMSMXXXXXMSXXAXAM
AAAAAAAXMASMSMXSMMSAMSMMXAMAMAMAAXMMMMSMSSMSAXAAAXAMSMSMXSAMMMSXMXSAMMMMXMAXAXMAMASXSMSSMAAXXSMMMMMXMXAMMSAMASAMMMXASMSSMMASAXASXSAMXMASMMXS
SSMMMMMXMMMAAMASXMMAMXAMSMSAMASMXSASAAMXMAAMXMMMMSSMAAMAASASXXMAAAMAMAXXXASMMSMXSAXAAAAMMSMAAXMXAMSMSMXAAMASAMAAXXSAMAAMAXXMASXMAMXMAMXSAMXA
MXXXXXASMXMSMMAMAXSAMMAMMASMSMSAAXAXMSAASMMMMSXXMAMMMSMMMXAMMXSXMSSMXAXXXMXSAAMAMXSSMMMSAMXMSMXMASAAAAMMXXXMMXMMXMASMMMSAMXMAMAMXMAMXSAMAMSM
MAMMSMXXAAMAMMMMMMMAMMMXSAMXMAMMMSSXAAMMXAXMASASMAMXSXMMSMMMAAMAMAMMMMMSAMAMSMSSMXAXAXXMXSXXMAASXMMSMSSMSSSMMXMXXMAAMXXMAXXMASAMASAMSMMSSMAX
MASXMSSMMMAAXAAASASMMASXMASXXAXAMAMMSMSMSAMXSMAMMSMXMASAAMASMXSAMAMAAAAXAMAMAXXAMSASXMXMMMMMMSMMAAXMAMXAAAAAAASMMMASXASAXSASASASASAMMAAAAXXA
SXXAAAXAAXMMSMSXSAAAMXSAMMMASASXMASXAXAXAXMXAMXXAMMAXAMMXXASXASASMSSSSSSXSXMSXSMMMAMMMAMAAAXAAAMXMMMAMMMMSMMSXXAXMAMAMMAMXAMASAMMSXMSMMSSMMA
MSMMMMXSMMXMAXXMMMMXMAXAXMMXAXAASAMMMSSSMSSSXSAMXSSSSSSXSMASXXMASAAAAAMXAMXAMAMXMMAMXXAMXXSXSSSMSXMMXXXXAMXAXXMSMMMSAXMAMMXMXMAMMXMMXAMXAAAX
AXXSAMAXAXSMMMSAXAAAMXSAMXXSMMXMMXMAMAAMAAAXMMAXXXAAAAAASAMXMXMASMMMMMMSAMMXMAMASMMAXMSSSXMAMXMASAASXMSSSMMSSSMXASASAMXSSMMSXSXMXAMMSSMMSSMS
MAMMASAMAMXAXASMMMMMXAXMASAMXMAXXXXAMXMMMMXMMSAMXMMMMMMXMXMAMXMASXSXXSASASASMSMASAMXSXMAAAMSMMSAMMMMAAAAAAAAXAASAMASXMAXAMASXSMMSASAAXMMAMMA
MAMSAMMSSMSSMASMSAMSMSMSXMAXAXMSMSSXSAXXAASAMAXSAAXXMXSXSAXAXAMASMSAMXASAMAXMAMMSAMAMXMAMXMASAMAXXXXMMMSMMMSSMMMXMMMMMXSAMXSAMAXSAMMXXAMAMXM
SAMMXMXMAXAXMXMAMASAAAAAXSMSMSMAAMAASMMMXMAMSAMSMXSAMAMXSASXSXSAMMMXMMXMAMMMSMSMSMMASMMMMMSASXSXMSMMSAXAAMAXXMAMAMAAASMMAMAMAMSMMAMMAMSXSSSX
MXMMMMSMMMSXMAMXSSMMSMSMAXAAAAMMSMMMMAAAMXAXMAMXMASXMASASXMAAXXAXSXSXMAMXMAAMXXAXXXXSAAMAMMMSAMAMXAASASXXMMXXMASAXMSMXAXXMMXXMAASAMMAMMAXXMX
AMMSMMAAAAXXSMSAMAAMXAMXAMXMSMSXMAXMSSMSAMMXSAMXMASASASMMAMXMMMMMSAMXSASASMSXSMMMXSAMXMSAMAXMASAMMXMXXMMMMSMAMAXMMMXAXSMSMSSSMSMMMSXMXMXMASM
SAAAAMSSMSSMXMAXSSMMMSMMASAAMASAXXMXAMXMMSAASASXMXSASAMXSAMAXAXAAMSMAMMSASXMASASASMMSAMXMSSSMASASXSMMASXAAAXAMSMSASMSMXAAAAASAAXAXSXSASASAMA
AMSSSMAAAXXAAMXMXMASXMXMASMSMAMMMSXMASMMASMASXMMSMMAMAMXSASXSSSXXXAMXXMMXMMSMSAMMSAMMAMSAAMAMASXMXAASAMXMMSSSSXASAXAAAMXMMMXMMMSSSMASASAMXSS
MXMAMMSMMMMSMXMSMSAMAMXMASXXMXMAAMAMXMAMAMXXMASAAMSASXMAXAXASXMMSSMXMASMMMMSAMXMAMMMSAMSMXSAMXMAXMSMMASMSXMAMMMMMAMSMSMXXMMMSXMAMAMXMMMXMAMA
XSMXMMMAXMMASAAAAMXSXMSMASASAMSMSSMXAXXMASMSXMASMXMASMXSXMMMMAMMXAMXSASAAMAMAMAMSSMAMAMXAXSMXSXMMAAAXXMAAMMMMSSXMXMXAAMXMXAAXAMASMMMAXSXMASM
SMMSAASAMXMAMMMMSMXMXAMXAMMMXAMXMAMSMSASAXAXAAMXXSMAMMAMAMASXSASMSMXMASMMSASXMAAMAMASXMMMMMAMXASMSSXMMSSMXXAAAMAXSMMSMSAASMSXXXAXMAXMMMASMSX
XASMMMSMSSMMMSASAMASXMMMMSSMXSMMMAMAAAXMMSSSMMXXAMMSMMAMAXXSAMMSAMXMMMMAXSASMSXXSAMXAASXMAAAMXSMAAAXSAMMXXMMMSSMMAAXAASXMMAAASMSSSSXMASMMMSM
MMMMAXMXAAXSASMSASAXXMMAMXAXXMAXSSSMSMXSXAXAMXMMAMAXMSMSMSMMAMXMAMMMAAMAMMXXAXAXXXXAXMMAMMSASXAMMMSMMAXSAMXAAXAASXMMMMMXSMMMSMAAAAAMSAMAMAMA
AAAMXMMMSSMMASAXXMMSSMSASMMMMMSMAMXMAMAMMMSMMASMMMSSXAMAAAAMSXXXAMASXMXAMXAMSMSMMSMSAXSAMMXAXXXMXXXXSMMMMMSMSMMMMAMXXASAXMAXXMMMMMMMXASMMAXS
SSMSAAMAMXMASMMMMAXAAASMSMXXXAAMXMMSAMXSAXMASXSAXAAMXSSMMMSSMMSMSXXMAMSMMMXMMAXAXAAAMMSAXXMMMMMMMMAMXMAAAAAMAXXAXXMXAMMASASMXMAMSXMMSMMMMMMM
XAASMMMSMMXSXMXASXMMSMMMMMSMMSSXSAASASMMMSSXMASXMMXSAXMXAMXAAXSAMXSMXMAMAMMXMASXMMSMXAXXMSXSAMAAAXAAASMSMSMSASXSSMAMAXSMMAAAAXAXXMMAMXAMASAX
MMMMAMAMAMMMAMXMSAAAAAAMAASAMXAAMMMMMMAAAMMXXAMAXXAMXSAASASMMAMAMASASMMSASMSMMMMMXMXSMSMMXASAXSSMSSSMSMAMAXMXSAAAAAXSAMAMXMSXSSXSAMASXMSASAS
MAAMXMASAMSSXMSXSXMMSSMSMSSSSMMMMASXSSSMSSSMMMSMMMXSAMAMXAXMAMSAMAMAAAASXSXMAAMXSAMAXAAASMMMSMXAAAMAXMMAMXXSAMXMAMMMMASXMMXMAAAAMMSASAMMASAA
SXSXXMXMXMAMMAMXSAMXXAXXXMMAXMASXAAXMAMAXXAMAMAAAAAMASXAMXMSAMXXSXMMMMMSMSASMMSAMASXMMMXMASAXXSMAMSXMMSMSMAMXSAXXAXXSAMXAXAMMMMMMAMMSAMMMMXM
AAMMXSSSSSSXMMMXXMMMSXMSXMMSMMMAAXMMMSMXMSXMASXSMSXSMMMAAAAMMSSXXAXMAMXMASAMXAMMSAMMSAXAXXMXSAMXXXXAMXAAAMAMMMMMMSSXMASMSMXSMXSXMASASMMXMAXX
MAMMAMAAAAAMSSMMXSAAXMXXASAMASXMSAMXAAMXAXASAMAXAMMXAAMASXSXAAMXSXMXXSMMXMASMMMAXASASASMSXMMMMMMASMSMAMSMSASAAAMAXMAMXMAMMMMMAMAMMMMSXSAMMSS
XSAMXSMMMMXMAAAMAXMXMAMSMMAMMXAAXXMMSMSXMSXMASMMXSXSMSSMXAMXMASMMMXSAAAMASXMAAMMSMMMMXMAAASAMASAASAMAMMMASXSMSMSMSSSMXMXMAAXMAXAMXAXXXMASAAM
MMXMAXXXXMAMMMMMMSMSXXAAXMXMASMMMXMAMASAMAXXXAXMXMAMSMAXMAMSXSXXAAAXMXMSASASMMSXSXSXMXMMSMSASASMSMMMAXXMAMXSAMASXAAMMMMAMXSSMMSASMMSMMSAMMSM
XSAXSSMXASXSSSXSXAXAAASMXSAMMMXASXMXSMSASMMMSMAMAMAMASAMXAMXXMASMMSSSMXXAXAMAXSAMAMAMXSAMXMMMMSXXAXSMMMMMSMMAMAMMXMMXASAXSAXAAXAMXXAAAXAXMMM
MMMMMAAMXMXAAAASXMMMSMMAXMAXXXMMMAXAMXSXMAAAAMASMMASAMXMSXMAMSASAAAXMASMMMSMMXMAMXMAMAMMSAMSSXMAMSMSAAXAAAAMXMXXMXAMXXMASMAMMMMSMMMSMMMSMMAS
AASASMMMSMMMMMSMAXSAMAMMMXXMSMSASAMXXXMASMMSMMASAXXMXSXMAMXXXMASMMXSMMMAAAXAXXSSMMMAMXSASXSAXMXMXMAXXMSMSSSMXMMAMSMMXMASMMMMAXMAASAAASXMASAS
SMSASXAXAASXXSAXXMMASXMSSSMMSAAAXSAMMMXAMXMMMMASMMSAXAMXMMSSSMMMXSSMMAXXMMXAMMMAASXSMAMMSMMMSMAMSMSMSMXAXAMXMMXSAAAMSAMXXAXSMSSSMMMMXXASAMXS
XAMAMMXMXAMXMXAMMMSXMASAAAAAMXMSMMSMASXMSXAAAMXMXAMAMXSXXXAAAXSAMXAASXSSSXSASXSMMMAMMMMXXAAXAMAMMAMAAAMSMMMSMMAMSSSMXAXAMMXXAAXMXXXSAMXMAMAS
MAMSMMXSMSSMSMXMAXMMSMMMSMMSMSMXASAMMSAMAAMXSSMSMSXXAXMASMMXMMAXSXMMMXXAAASAAASXSMMMAXXMMSSSSSSSMAMSMXMXASASAMXMAXXMSMMMMSAMMMSAMXAAXAAMXMXM
SSMMXSAXXXAASXSXSAXMAXMAXMMAMAMXMSASASAMMXMAMAAXAMMMSSMASAMSSXMASMSSXSMMMMMMMMMAMSXSMMSAMAMMXAXXXAMAMXXSMMASAMSMSMMMMXAXMXMSXXXMAMXAMSXMASAM
SAAAAMXSMMMMMAMAXMMXMSMXSAMASASMXXAMXSXMXAMMSMMMAMAAAXMAXAXAAAXAXXMSAMAAMSASXSMSMXMXMAMSMASXMSMSSSSMMXMAAMXMAMXMASAAMMSSMAMMAMXMXAXSMMXMASAS
XSMMSSMMXMAMMMMSMXSAMXMMMXMASAXXSMAMAXMASMMASAMXXSSMMMMSSMMSSXMASMMMMMSMMSAXAXMASAMXMASXSMMMMMAXSXAAAXSXMMMXAMXMASMXSAAAXASAAMAMMSMMASXSXSMM
MMMSAXAAAXAMAAXXAASAMMMXAMMMMMMAMXAMXSSXMAMASAMMAMAXXSXMAMAXMASAMXAAXXXMMMSMAMSASMSXMMSAMXAAAMXMMSSMMXMMSAAMSSSMAXMAMXMSAMXXSSXSAMASAMAXAMXS
AAXMASMMXSMSXSXMMMXAMXAMSSSMAXMAMSXMXMMMSMMAMAMXAMXMMAMMAMSXMXAMXSXMXXXXAAXMXMMASAAMMMSMSSXSSSXSAAXASASASMSMAAAMSMMXSMSMASMMXMXMASAMMSMMSMMX
MAMMXMAAXSAMAMAASXSMMMXSMAAMMMMAXSXSAAAAAAMSXSMSSMSAXMMSSSXASAMXXMAMSMMMMSMMASMMMMMSAAXAXXAMAMXMMSMXXAMAMAMXMSMMAASASMAXAXXMASXSMMMSMAMAXAXX
AAXAAXMASMAMAMXMAMXAAMXSMSMMMSXMAXMASMMSMSMXAAMSAAMSMXMAMXXXMAMMMSXMAAMSMMMSAXSMXSASMSMXMMXMAMXSAXXAMSMSMSAMXAAMSSMAMMSSXMAMXSAMSMXAMASXMMMS
SASMMSMSMXAMSSXMXASXXMASMXAMXSAMXSXMXXXAXMAMXMMMMMMMMSMMSXSSSSMAMAXSSSMSAAMMSMAXXMASAXMASMMSXMAMASMMMXAXMAMMMSMMXXMAMAXXMXSSXMXMAMMMSXSASMAX
MXSXSAMXMSSSMMMSMMMSAMASXMASAMXMAMAMMSMSSMAMSSXSASXMAAMXSAMMAXSXMAXAAMASMMMAMMXMMMMMMASAXAXAMMAMXMASAMSMSMMSAMASMMXSMMSAMAMMMSASASAMXAMAAMXS
MAMXMASXAAMXAAAAAAAXMMXSXXMXMMSMMSAMMMAAXXXMASASASAMSMSAMAMMXMMMASMMSMAMAMMASAMXAAXAMMMSMSMMXSXSXSAMASAAXAAMAXAMAXAXAASAMMXAASXMASXXXXMXMAMX
MAMASMMMMMSMSMSSSMSMSAMMMXSAAMAAMSXSAMMMSAMXMXMMAMMMXAMXSSMXXAXAAMXXAMSSSMMAMXSXSMSASMAXMXAXAMAAAMASMMMMMMMXAMSSSMMSMMSAMXMMXXMSMSASXSMMXSMM
SXSXSAAXMASAMMMMXAAAXMAMSASXSSMSMXXSASXSMMMSMMMMXMXAMAMMAMMMSSSMSSMSMSMAXSMXSXSAMAXXAMXMASMMMSAMXMXMASXSMXSMXSXAXXMAMASMMAASMMAAAMMMAASAAXAX
AMMXMXMMMASMSMSSMSMSMMMXMAMXXAMAMXXMAMXAAAAAXAAAAMMMMAMXAXAXSXAXAXXAXAMMMXMMAAMXMAMXMASMAMAAAXMXXSASMMAAMASXSAMXMMSAXXMAXMMAASXMMMAMSMMMMSMM
XASMSMXAMXSXMAAXMAAAASXMMAMSSMMAMMMMAMMSSMSSXSXSXSASAAMSXXXSMSMMMSSMSXSASAMAMXMMMXSXSXMMSSSMSSMSMXASXMXMMASXSMSAMXSXSSSSMMSSMMASMMXMXAXXAAXM
MSXMAMSMSASAMMMSSMSMXMAAMMXMAMSAXAASAMAAXXMMAXAMASASXSXMSAMXMAXAMXMXMASMSAMAMAMSMMAMMSMAMXXAXMAAAMSMMMSXMASMXASXSAMXMAAAAAAAXSAMXMSAMXMMSSSX
SMMSAMMAMASAMXXXMAXXXSMMMSMMSMSASMMSAXMASAXXAMAMMMAMMMAAXXMAMMMAMAMMSMXXSAMXSASASAMAAAMAMMXMMMSMMXAAAAAXAXXAMXMAMMSXMMMMMMSSMMMXSAMMSMXXXAMX
AMASMMMXMXSAMXXAMSSSMSAMASAAAAXAXXXMXMXMAXMMXMAMXMAMAMMMMASXSSSSXMSAMXMXSXMASXSMSSXMSSSXSXAXAXXASXSSMSSXXAMSASMXMMAMXAMASXAMXMAAMASMAMMSMSMS
MMMMAXSMXMSXMSXMXAAMASMMASMMMSMSMSMSMMMMSXXAMSSSMSSSMXAAMAMMXAAAASMMMASXMASXMASXMASMXAXMMXSSMXMAMAAAAXMMSXMAAMXAXMAXMASAXMMMAMMMSAMMAMMMAAAX
XSXSMMAASMMXXMASMMSMAMXMMSXSMXAAAAXAMAAXMASMXAMAAMAAXSXMMAXAMMMMMMASMMSASASAMAMAMMMMMXMXXAMAMSMAMMMMXMAAMASMSXMSXMXSAXMXSAASASAMMXSSMSSMSMXM
MXXSXMSSMAASMSAMAAAMXSAMAXAXAMSMSMSMXSXSXAMXMASMMMMMMMASMMXSAAMSMMAMAASXMAXMMMSMMMAXXMAMMMSAMASMMXXXAXMMSAMAMMAXMSAMXMAXXXMMXMAXSAXMAXAAXAMX
ASMSAXMAXXMSAMXXMMMMXMASXMMMXMAAAAAXMMAXMMSSSMSAXXAXAMAMAAAMMXMAMMMSMMMMMSMAAAAAAXXMXMSAAASXSASMSSSSSSSMMMMAMMMSAMASAMSMSMSMMSSXMASMSMMMSAMX
XMASAMXAMMXMMMMSSMSXMSMMAXSSSSMSMSMSASAMAXAAAASAMSSSMMSSMMMSMMSXXAMSXAXMAMMMMXMXMMSXSAMXSMMAMASAXAAAAXXXAASMSAXAMSAMMXAAAAMMAXMASAAAAAAAMAMX
XMXMMXMASXMXAMXMAAXSAASMXMXXAAAAAXAMAMAMXSMSMMMAMAAAXAXAMXAAAMAXMAMSMSAMXSASXMMSAXAAMAMMMAMAMMMMMMMMMMSMSXSAMMSMMMASXSMSMXMMXSSXMMSMSMMXSMXS
XXMASAXAXAMSAMXSMMMASMXXAXXMMMMMSMXMAXAMXMAMXXSMMMSMMXSASMMSSMASMSMSAXXSASMAAAASMMMXMXMASXMMMAAAAXSAXAXMMAMXSXMXAMMMAAAMAMSSMMXMAMMAMMMXAXAM
MMSXMAMXSAMXAMAXXXXMXSXMMAMSXXXXXMMSMSXSAMSMXMAMXMMXSMMAMXAAXMMMAAAMSMSMAXXSMMMSXAAXXXSXSMMASMSSMSMSMMSAMXMMSAMSMSSMSMMMAMAAXSASAMXAAAMSMMXS
SASAAXAXMAMXXMSSMMSXAXMASAAAMASAAXAAAAXMXMXAMXMSAXSAAAMSMMMSSSMMMMMMMXMMAMXXMASXMXSSMASMMXSASXAXMSAMXMMXMAAASAMXAAXAXAXXAMXMMSASASMSMMXAASMS
MASMMXSXSSMMXXAAAAMMMSAXSAXXSASMMMSXSSMAAXMSMAMSASMAMXAXAXXXAXXAMXMMMAMAMMSASXSAXXAAXAMAMAMASMMMAMMMMXASXMMXSAMMMMSMSMMSSMXXMMAMASXMXXMSSMAS
MMMMMXAAAXMASMMSMMSAMMXMMXMXMMMXMAMMMAMSMMAMMXMMXMMAMMSSMMMMMMMMASAMSASMMASAMAMMMSSMMSXXMMSASAMSSSMAMMXXAXMAMAXXAAAAAXAXAAASXMMMXMASXMXXXMAM
MAAAMXMMMSAMXAXAXAMASAXSAMXXMMSSMXSAXAMASMMSMMXMMAMASXAAAAMSXSASMMAXSAXAMXSAMMMMXXAAAAASMXMASAMAAMXAXMASMMMMSAMXASMSAMXXXMMSAMXXASXMXMAMMMMS
SMSSSSXSXMMXXSMAMXSXMASMSMMMSAAAAXXMSASASXAAAMXSMASMXMSSMMXSASASXSMMSMSSMASAXSAMXSMMMMSAAAMMMXMMSMSMMSAAASAMXAMXAMMMXSMSXMAXXASMXXXMAXAXMAMS
AXMAXMAMXSSSMXMXMMMMMXMAAXMASMSMMMAMSXMASMSSSMASMMMMMAAMASXMAMAMAAMAXMAAMXSAMSAMXAAAAXMMAMXSASXXXAXMAMMMAMXSMAMAXMAMAAAAAMSSMMAASMASXSXMXAXX
XASXSMSMAMAAAMMAAAMXMAMSMSMMXXXAXXXMMAMAMAMAAMXSAMAAMXMSAMXMMMAXSMMSMMSSMAMAMSXMXXXMXSSXSXXMAMAMMSMMMSSMMXMAMXXSSMSMAMSMXMMAMXMASMXXAAMSSSSM
MXMASAMMASXMMSSSXMSMMAMMASMMMSSSMMMMSAMXXMAMXMASAMXSAMMXMASMASXMMXXAXMMMMXSSMMMMXMMSXMXAMXXMAMXMAMAMAAAXSAMXXMMMAAMXSAMXAMXAMXXXMXMMMMMXAXMA
AASXMAMSMMAMXXAAMSAMMSSMAMAAAMAMAMSASASMSMSAAMASXMAXMAMAMMMXAMASXSSMMSAXXMAMXMASMMAMAMMXMAMXSAAMXSAMMSSMSASXAAASMMMAXAMSSSXXSSMMMAXAXXSMMMAS
SASAMMMASMAMAMMMMSASXAAXSSSMXSASAMMASASAAAASXMASAMASXSSMXXAMSXMMAAMAAMMMMMSMMMSMSMASAMMSMASMMSASASXSXMAASAMXASXSAAMMXAMSXSAAMMMASASMSMXAAAMA
MAMMMXXAXSAMXMASXMAMMSMMMXAAAXXMAMMMMAMXMXMMMMASXSMSXMAMAMSXXAMMSMMMMXSAMAAAASAAASMSXXMASASAMAXMAMXMAMMMMAMSXMASXMXSSSMSAMMSMASMSASASMSSXSMM
MSMSASMMMSMMAMXXXMAMXMASXAMMMSMSXMSAMXMXSXAASMMSAAMMASAMXAMASXMAMAMXMASASXSMMMMSMMXMAMSAMMSAMMAMAMASAMXASAXSAMMMMSAMXXAMSMAAXXSAMMMASXAAMMAX
XMXMASXXAXASMSXMASASXMASMXSAXAAMSASASMSAMSSMMAXMXMAMXMXSMXMAMAMXSAMXMASXMXXAMXXXXSMSAXMASAXAMXXSSSMSASMMSXMMXMXAAMMSAMXMXMSMSMSMSXMASMXSASMM
XSASXXMMSMXAMXMAMSXSAMAXMAMXMMSMMXSXMAMXMAMASMMSMSXMSAMXAXMAXXMASAMXMASMSAMXMMSAXMASMMXXMASXMSMMAAXXXMAAMAAXAXSMSXXXMAMXMXMXSASASXMAMXMAXXXX
MSAXXAMXMSAAAXASAMXSXMXSMMSMSMMXMXMXMMMSMASMMMAAAMAMXAXSSSSMSMMXSAMSMMSAMAMXSAMXMMMMASXMMMAMXXAMMMSSMMSASXMXMXAMAMSMSSSMAAMXMAMAMXMASMXMASMX
AMXMXSMAXAMAMXXMASAXAXMAXAAXAMMAMAMAMASAMAMAAXSMSSXMSSMMAAXAAXMAMAMXAAMMMASMMXSAMXAMAMAAMASMMSSMXAAXAMXXMASAXXAMXMAAAAAASAXAMAMAMXSAMMAMAAAX
SSMSAMASMMXSMSMSAAMSXSXAMXXMMXSASASASXSASMSSMXMXMAAXAMASMMMSMMMAXAMSMMSMMMXAAAMAMSASXSXMMAMAAMAXMASXSAMXMAMMSXMMSMMMMXMAXASMSMSSMMMAXMAMMMXM
XXAMASMMAXMMAAAMMSMAAMMSSSXSXAXASXSXSMSAMXMXMAMAMXAMXSAMAXXXMAXSSXXAAAAAAMSMMXSAXSAMXAXAMXSMMMMXMAXMXMXAMXSAMASAMXSMMXMASMMAAMAMAXSMMSSSSSSM
XMXMXMAXXMAMMMMMAAAMAMAAAXAMMMSMMMSMSAMXMMSMSASXSAMXXMAMXMXMASXAAMSSSSSSMMAMAMMMMMAMMASMSASMAMXMMAMXAMSASAMASXMASAMAMXMAXMXXMMAMSMSXAXAAXAAA
SMMSMAASMMMSXSMMXASMMAMSMMSMAAAAMXSASMMASXAAMMXAMXMMMSSMMAASAXMMMMXAAAMAMSMMMSAMMSMMXAAXXAXXAMASXSXSMMAXMMSMMXSMMXXAMXMMSSXMXMXMXAMMSMMMMSMM
SAAAAMMSAAASMXXASMMXXAXAMXASMSSSMAMXMASAXMXSSSSMSASAMAMAXSXSAMMSAMMMMMMMMAAAAXAMAAXXMMSSMAMSSSMSAMMAMAMXSXMMXAAMAXXSSMSAAAAXAMXMMAMAMAAMMXAX
SMMSXAMSMMMSASMMSAASXXXAAXAXMAXAMMSMSMMXXSAAXXAASASMMASMMMXMXMASASXAXAAAMXSMSMSMSSSMSAAAXXMSAAAMXMAMSAMMMASXMMSMSSMMAMMMSMASASAAMAMASMMSAMXM
XAAMMXMMAXAXMAAASMMMASMAMSMXASXMMAAAAXXMAMMXMMMMMAMXSXXXASXXAMAMAMMMSSSXSAMAXAAMAAMAMMXSMSSXSMMSAMMMXASXMAMXXMAMAAAXAMAXAMASASXSMAXXXAAMMSAM
SMSXSAASMMSMMSMMXAXMAMAMXAMMMMAXMSSSMMSAAXSASAAXMXMASMMSMMMXXMSSXSAXXAAAMAMAMSMMMSMSMSXXAMXAXXXSASMSXMAMMAMMMMMSSSMSSSXSMMMSASAMXSMSXSMSASAS
XAAAXSXMMAXAAXXMXSMMXSXMSAXAASXMMXAAAAAXXMSASAXSXMAMMXAAAASMAXAAASMMXMMMMMMXMAXXXAAAAXAMSMMAMXMSAMAAMSASXSMSAAXAAAAAXXXMXMMMMMASAMAMAAAMAXAM
MMMSMMMMMAMMXMASAAASAMAMXMSSMMSMMMMMMMSSSMMMMXMSAAXXSMSMMMXAXAMMMMASMXAXASMSMMSSSMSMSMMMAXSAMMAMXMXMMMAMAAASXXMMXMMMSMMSMMXAXSAMXMAMSMMMSMAM
XXAMASAMMMSMXSAMASXSASAMAMXMAMXMXMASXAXAAMXASAMMAMMMXAAXSSMSSMXAASAMAXMSXSAASAAAAXAXMASMXMSASAXAASASMMXMMMMMMSMSXMAXAAMAAMSSMMASXMXMXASAXSXM
XMASXMSXAAAXXMMXMXMSAMXSASMSXMXSAMXMASMSMMSASASXSMMAMMMSAASAAMMMMMMSMSAMXMXMMMSSMMMXSMMXMXXAMXXSXMAMMASMSSMMAAAXASMXSMMSSMAMXSSMMSSXMAMXMAMX
ASAMMMAMMXSXMMSAMAMMSMAMXSAMAMASAXAXAXAMXMXXMAMXAAXMMMMMXMMSSMMSAMXAAMMXSMXXXAAAAAXMSAMMSAMSMSXMXMAMMASMAMAMSSSMMMSXXAAAXMASXMAXMASXMSAMXXAS
MMMXAAMMSAXAAASMXXSAMMMSMXASAMASAMSMSSSMAMSSMAMSSMMSMAAAMXMAXAASASMMSMMXMASXMMSSMMMAXASAMXXAAXMAASAMMMXMAMXMAAAASASMSMMSXXMXAMMXMASXMAAXMASA
MAAMXMXAMASXMMSXSXMMSXSAMXAMMMAMAMMAAAASXSAAXAMXAAAAMSMXSAMSSMMSXMXXMAXAMAMAAMAMAASMSMMXSMSMSMMSMSASASMSXSAMXMMMMASASMAMMSSSMMMAMXXAMMMMMMXM
MSSSMASAMXMAXXXAAXAASMSASMSMXMASMMMMMSMMMMXSMSSSMMXSMXAXSAMXAXAXMAXAMMSSSSSSMMASMMMAAXAAXMAMXXMMXSASASAAMSXSXSMXMMMXXMAXXXAASMSSSXSAMASMSAMX
XAAAXASAMMSMMXMAMMMXSASAMAMASXMSMXXXXMASXAAXAXXAAAAXMMSMSMMSMMSSSSMSXAXXAMMAAMASAMXMSMMSXSASXSXXAMXMAMMMXSAMAXMASASXMMMSMMMMMXAXAAXAMXXAAXXM
MMSMMAXAMXAAXXMAMMMMMMMMMXMAXAMMMMSAMXMSAMXMAMSSMMMSAAMASAAAAAXMAAAMMMMMSMSMMMMSAMMMXAXMASMSAMMMMMMMXMXMXMAMXMSXSAXXAAAAMMMAXMMMMMMSSSMSMSSS
XAAXAMSMMSSSMMMASAAAAXAXAXMSSSMAAXAMXSXSXSXMAMMAMMMSMMSAMMSSMMXMMMMMAXXAXMSAMXASAMXAXAMXXMAMXMAAXAAMMSSMMSSMAMMMMMMSSMSXMASXSASMSAXMAXAMAAAA
MSSSSMAAXAAAMASAMXXXMSMMSAMXAAXMMSMMMSAMASXSAASAMAMMMAMASAAAASXMSMXSSXMXSASMMMMSSXMASXMSSSMSASMSSSSSXMAAMAASASAXXSAAAMXAMXSMSAMASMXMMMXMMMSM
MAAMMSMSMMMMMXMMSSMSAAAXMMAMMMSSXAAMASAMAMMMSXXXSASMMASXMMSSSMSAAXAMMAMAMMMSXAXMMXAAAXAAAAASXXMXAMXMASXMMXXSSSMSXMMSSMSSMAMASAMXMAMMXSXMXAAA
MSXSAMXAMSASMMMMAMAAXMAMXMAMXAAMXSMMASAMXSAMMXSXSASAMXMAMAAMAAMSMMXMMAMMSMAASXXXSSSXMMMMXMMMMSMMASXSAMASXXXXXXMSMSAXXAAXMAMXSAMXXMASAMMMSSSS
XXAMXXSAXSASAAAMASXMAXSMMXAMMMSSMXAMASAMXMXAAASMMAMXMASAMMXSMMMXXAXMXMSMAMSMXSXAMXAAAMAXSAMXAAAMAMAMXSXMSMMMMMMXAMMSMMMXXAXAMAMMXSXMASAXMAAX
XMSMXXMMMMMMMSXSMSAXSXMASXSSSXAXXMAMXSXMXXAMMMXAMXMSSXSMXSAAAAAAMSMSAMAXXXXMAAMMMASMXXASMXMASXSMMMAMMMMMAMAAAAAMSMAAXAAXMXMSMSMSAXASASXSMMMM
MMAMXMAAXAAXXXAAAXXMMAMAMXAAXMMSSMMSAMASMSMXAXMXMAMASMXMAMMXMMXMSAAXASASMMAMXMXAAXMXXMXMMASAMAAAXSAMXAASASMSSSMMXMSSSMSSXSAMAAAMASMMMXASMAMA
XMAXASXMSSXSAMMMSMAAMXMAMMMMMSAAAAAMAMMXAAASMSAASXMASXMMASMSXSAMXASXXMASASAMXSSMSSMMXMSASXSAMMMMMAAMSMMSASAXMAXMAMMMMMAAASAMAMXMAMMAMMMMAAXS
XSSSXXSAAAXMAMXAAXSMAASASAXAAMMSSMMSAMXMMMXMAMXXMAMASASAMXAAASXMSAMXMMXMAMASAMXXAAASAXSAMASXMXMSXMAMAAMMAMMMMAASASAAAMMSMMAMXXXXXASAMXMASMSA
MAASMSAMXSXASAMSSMXMSMSASXSMSSXMAXXSMSXXSMAMXMMMAAMMSMMMAMMMMMSMMASXMASXSSSMASAXSSMMXXMMMMMXMASAXXXSSSMMMMXMMSMSASXSXSAMMSXMAXSAMXSXSAXMASXX"""

small_inputs = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""
part_2(small_inputs)