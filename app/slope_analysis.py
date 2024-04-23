from pyslope import (
    Slope,
    Material,
    Udl,
    LineLoad,
)
from model import (GeologyModel, UdlModel, PointLoadModel, LandModel)

def show_full_calculation(land_model : LandModel):

    s = Slope(height=land_model.slope_height, length=land_model.slope_len)

    materials = []

    for g in land_model.geology:
        materials.append(
            Material(
                unit_weight=g.unit_weight,
                friction_angle=g.friction_angle,
                cohesion=g.effective_cohesion,
                depth_to_bottom=g.layer_thick
            )
        )


    s.set_materials(*materials)

    udls = []

    for u in land_model.udl:
        udls.append(
            Udl(
                magnitude=u.magnitude,
                offset=u.offset_from_crest,
                length=u.load_len
            )
        )

    s.set_udls(udls)

    line_loads = []

    for l in land_model.point_load:
        line_loads.append(
            LineLoad(
                magnitude=l.magnitude,
                offset=l.offsetFromCrest,
            )
        )

    s.set_lls(line_loads)

    s.set_water_table(land_model.water_depth)

    s.set_analysis_limits(s.get_top_coordinates()[0] - 5, s.get_bottom_coordinates()[0] + 5)

    s.analyse_slope()

    print('fos:',s.get_min_FOS())

    # fig_1 = s.plot_critical()

    return s.plot_all_planes(max_fos=2)
    
