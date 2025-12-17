def read_input(filename):
    with open(filename) as f:
        lines = [l.rstrip() for l in f if l.strip()]
    shapes = {}
    regions = []
    i = 0
    while ":" in lines[i] and "x" not in lines[i]:
        idx = int(lines[i][:-1])
        i += 1
        shape = []
        while i < len(lines) and all(c in "#." for c in lines[i]):
            shape.append(lines[i])
            i += 1
        shapes[idx] = shape
    while i < len(lines):
        dims, counts = lines[i].split(":")
        w, h = map(int, dims.split("x"))
        counts = list(map(int, counts.strip().split()))
        regions.append((w, h, counts))
        i += 1
    return shapes, regions

def parse_shape(shape):
    return [(x,y) for y,row in enumerate(shape) for x,cell in enumerate(row) if cell == "#"]

def normalize(occupied_cells):
    min_x = min(x for x, y in occupied_cells)
    min_y = min(y for x, y in occupied_cells)
    return tuple(sorted((x - min_x, y - min_y) for x, y in occupied_cells))

def generate_orientations(occupied_cells):
    unique_orientations = set()
    for scale_x, scale_y in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        for rotation_count in range(4):
            transformed = []
            for x, y in occupied_cells:
                rx, ry = x, y
                for _ in range(rotation_count):
                    rx, ry = ry, -rx
                transformed.append((scale_x * rx, scale_y * ry))
            unique_orientations.add(normalize(transformed))
    return list(unique_orientations)

def area_check(board_width, board_height, shape_orientations, piece_counts):
    used_area = sum(len(shape_orientations[shape_id][0]) * count for shape_id, count in piece_counts.items())
    return used_area <= board_width * board_height

def parity_check(board_width, board_height, shape_orientations, piece_counts):
    checkerboard = [[(x + y) % 2 for x in range(board_width)] for y in range(board_height)]
    required = [0, 0]
    for shape_id, count in piece_counts.items():
        base_shape = shape_orientations[shape_id][0]
        black = sum((x + y) % 2 for x, y in base_shape)
        white = len(base_shape) - black
        required[0] += black * count
        required[1] += white * count
    total_black = sum(row.count(1) for row in checkerboard)
    total_white = board_width * board_height - total_black
    return required[0] <= total_black and required[1] <= total_white

def can_pack(board_width, board_height, shape_orientations, piece_counts):
    if not area_check(board_width, board_height, shape_orientations, piece_counts):
        return False
    if not parity_check(board_width, board_height, shape_orientations, piece_counts):
        return False
    board_filled = [[False] * board_width for _ in range(board_height)]
    pieces_to_place = []
    for shape_id, count in piece_counts.items():
        pieces_to_place.extend([shape_id] * count)
    pieces_to_place.sort(key=lambda sid: -len(shape_orientations[sid][0]))
    valid_placements = {}
    for shape_id in set(pieces_to_place):
        placements_for_shape = []
        for orientation in shape_orientations[shape_id]:
            max_x = max(x for x, y in orientation)
            max_y = max(y for x, y in orientation)
            for y in range(board_height - max_y):
                for x in range(board_width - max_x):
                    placements_for_shape.append([(x + dx, y + dy) for dx, dy in orientation])
        valid_placements[shape_id] = placements_for_shape

    def place_pieces(piece_index):
        if piece_index == len(pieces_to_place):
            return True
        shape_id = pieces_to_place[piece_index]
        for placement in valid_placements[shape_id]:
            if all(not board_filled[y][x] for x, y in placement):
                for x, y in placement:
                    board_filled[y][x] = True
                if place_pieces(piece_index + 1):
                    return True
                for x, y in placement:
                    board_filled[y][x] = False
        return False
    return place_pieces(0)

def solve(filename):
    shapes_raw, regions_data = read_input(filename)
    shape_orientations = {}
    for shape_id, ascii_shape in shapes_raw.items():
        shape_orientations[shape_id] = generate_orientations(parse_shape(ascii_shape))
    solvable_regions = 0
    for board_width, board_height, counts_list in regions_data:
        piece_counts = {shape_id: counts_list[shape_id] for shape_id in range(len(counts_list)) if counts_list[shape_id] > 0}
        if can_pack(board_width, board_height, shape_orientations, piece_counts):
            solvable_regions += 1
    return solvable_regions
print(solve("input.txt"))