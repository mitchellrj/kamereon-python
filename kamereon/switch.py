"""Support for Kamereon switches."""
import logging

from homeassistant.helpers.entity import ToggleEntity

from . import DATA_KEY, KamereonEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, vin=None):
    """Set up a Kamereon car switch."""
    if vin is None:
        return
    vehicle = hass.data[DATA_KEY][vin]
    #async_add_entities([KamereonSwitch(discovery_info)])


class KamereonSwitch(KamereonEntity, ToggleEntity):
    """Representation of a Kamereon car switch."""

    @property
    def _switch(self):
        return NotImplemented

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        await self.instrument.turn_on()

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        await self.instrument.turn_off()