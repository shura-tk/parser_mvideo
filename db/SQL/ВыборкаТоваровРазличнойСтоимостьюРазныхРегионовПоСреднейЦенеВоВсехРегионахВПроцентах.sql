SELECT two.name, ((AVG(one.sale_price) - MIN(one.sale_price))*100/AVG(one.sale_price)) AS sale, MIN(one.sale_price), MAX(one.sale_price)
FROM public.prices AS one
LEFT JOIN public.products AS two ON two.product_id = one.product_id
WHERE one.product_status = 'Available'
GROUP BY two.name
HAVING MIN(one.sale_price) <> MAX(one.sale_price)
ORDER BY sale DESC
	