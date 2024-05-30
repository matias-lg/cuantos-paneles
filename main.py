def max_panels(panel_dimentions: tuple[int, int], roof_dimentions: tuple[int, int]) -> int:
    [panel_width, panel_height] = panel_dimentions
    [roof_width, roof_height] = roof_dimentions

    # panel en su orientación original y rotado en 90°
    orientations = [(panel_width, panel_height), (panel_height, panel_width)]

    for pw, ph in orientations:
        horizontal_stacked = roof_width//pw
        vertical_stacked = roof_height//ph
        if horizontal_stacked == 0 or vertical_stacked == 0:
            continue
        if horizontal_stacked > vertical_stacked:
            return horizontal_stacked + max_panels((panel_width, panel_height), (roof_width, roof_height-ph)) 
        else:
            return vertical_stacked + max_panels((panel_width, panel_height), (roof_width-pw, roof_height))

    return 0



if __name__ == "__main__":
    testcases = [
            # casos de prueba publicados
            [(1,2), (5,3), 7],
            [(1,2), (2,4), 4],
            [(2,2), (1,10), 0],
            # ...otros adicionales
            [(1,1), (10,10), 100],
            [(10,10), (1,1), 0]
            ]

    for [panels_dim, roof_dim, expected] in testcases:
        assert max_panels(panels_dim, roof_dim) == expected
    print("Todos los test pasaron 😎")

