from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from django.conf import settings


class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Añadir'),
            children=[
                {
                    'title': _('Nueva Receta'),
                    'url': 'loptique/receta/add/',
                    'external': False,
                },
                {
                    'title': _('Nueva Venta Varios'),
                    'url': 'loptique/venta_varios/add/',
                    'external': False,
                },
                {
                    'title': _('Agregar Transaccion'),
                    'url': 'loptique/transaccion/add/',
                    'external': False,
                },

            ],
            column=0,
            order=0
        ))
        self.children.append(modules.LinkList(
            _('Ver'),
            children=[
                {
                    'title': _('Ver Productos'),
                    'url': 'loptique/producto/',
                    'external': False,
                },
                {
                    'title': _('Ver Recetas'),
                    'url': 'loptique/receta/',
                    'external': False,
                },
                {
                    'title': _('Ver Ventas Varios'),
                    'url': 'loptique/venta_varios/',
                    'external': False,
                },
                {
                    'title': _('Ver Transacciones'),
                    'url': 'loptique/transaccion/',
                    'external': False,
                },
            ],
            column=0,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Models'),
            exclude=('auth.*',),
            column=0,
            order=0
        ))
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            10,
            column=0,
            order=0
        ))