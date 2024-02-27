SELECT
	pr.product_id,
    pr.name,
    pr.uom_id,
    uom.uom_name,
    pr.price_per_unit
FROM grocery_store.products as pr
LEFT JOIN grocery_store.units_of_measure as uom ON uom.uom_id = pr.uom_id;

INSERT INTO grocery_store.products (name, uom_id, price_per_unit) VALUES ('pepper', 1, '22.56');