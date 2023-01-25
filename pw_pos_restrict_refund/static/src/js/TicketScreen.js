odoo.define('pw_pos_restrict_refund.TicketScreen', function (require) {
    'use strict';

    const TicketScreen = require('point_of_sale.TicketScreen');
    const Registries = require('point_of_sale.Registries');
    var rpc = require('web.rpc');

    const { _t } = require('web.core');

    const PWTicketScreen = (TicketScreen) =>
        class extends TicketScreen {
            async _onDoRefund() {
                if(this.env.pos.config.pw_allow_refund) {
                    const { confirmed, payload: inputPin } = await this.showPopup('NumberPopup', {
                        isPassword: true,
                        title: this.env._t('Password ?'),
                        startingValue: null,
                    });
                    if (!confirmed) return;
                    if (inputPin == this.env.pos.config.pw_refund_password) {
                        super._onDoRefund()
                    } else {
                        await this.showPopup('ErrorPopup', {
                            title: this.env._t('Incorrect Password'),
                        });
                        return;
                    }
                }
                else {
                    super._onDoRefund()
                }
            }
        };

    Registries.Component.extend(TicketScreen, PWTicketScreen);

    return TicketScreen;
});
