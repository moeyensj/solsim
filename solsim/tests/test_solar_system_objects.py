from .. import solar_system_objects as sso
import pytest

classes = [sso.SolarSystemObject, sso.Star, sso.Planet, sso.GasPlanet,
           sso.TerrestrialPlanet, sso.DwarfPlanet, sso.Asteroid, sso.Comet]


def test_bad_position() :
	with pytest.raises(TypeError) :
		for class_ in classes[((classes != sso.Star))] :
			_ = class_(200., 2., [20., 30.])
			_ = class_(200., [2.], [20., 30.])


def test_bad_velocity() :
	with pytest.raises(TypeError) :
		for class_ in classes[((classes != sso.Star))] :
			_ = class_(200., [2., 6.], 20.)
			_ = class_(200., [2., 6.], [20.])
