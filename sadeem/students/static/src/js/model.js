/* ================================================================
  ||                 My Model : override PosModel
   ================================================================
 */

odoo.define('students.model', function (require) {
'use strict';
var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
var _super_posmodel = models.PosModel.prototype;


models.PosModel = models.PosModel.extend({
    initialize: function (session , attributes) {
        // new code
        var partner_model = _.find(this.models , function (model) {
            return model.model === 'res.partner';
        });
        partner_model.fields.push('membership_code');

        console.log("Hi from 1");
        // Inheritance
        return _super_posmodel.initialize.call(this , session , attributes);
    },
});
console.log("Hi from 2");

});