# -*- coding: utf-8 -*-
##############################################################################
#
#    Ingenieria ADHOC - ADHOC SA
#    https://launchpad.net/~ingenieria-adhoc
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _

class account_voucher_receipt(osv.osv):
    _inherit = 'account.voucher.receipt'
        
    def receipt_print(self, cr, uid, ids, context=None):
        '''
        This function prints the receipt
        '''
        report_obj = self.pool.get('ir.actions.report.xml')
        report_name = report_obj.get_report_name(cr, uid, 'account.voucher.receipt', ids, context=context)
            
        return self.pool['report'].get_action(cr, uid, ids, report_name, context=context)
