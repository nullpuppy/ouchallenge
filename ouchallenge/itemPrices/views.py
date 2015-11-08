from itemPrices.models import ItemSale
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count


class ItemPriceService(APIView):
    """
    """
    def get(self, request):
        # need request.query_params(item, city)
        item = request.query_params.get('item')
        city = request.query_params.get('city')

        if not item and not city:
            # error state
            res = {
                'status': 404,
                'content': {
                    'message': 'Not Found',
                }
            }
            return Response(res)

        query = ItemSale.objects
        if item:
            query = query.filter(title__startswith=item)
        if city:
            query = query.filter(city=city)

        # Get total item count for given parameters.
        count = query.count()

        # Find list_price mode for given parameters.
        query = query.order_by('list_price').values('list_price').annotate(price_count=Count('list_price'))
        price_mode = query.order_by('-price_count', '-list_price').first()
        if price_mode:
            price_mode = price_mode.get('list_price')

        res = {
            'status': 200,
            'content': {
                'item': item or 'Not specified',
                'item_count': count,
                'price_suggestion': price_mode,
                'city': city or 'Not specified',
            }
        }

        return Response(res)

