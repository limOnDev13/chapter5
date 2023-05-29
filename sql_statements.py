CREATE_BRAND_TABLE = \
    """
    CREATE SEQUENCE brand_id_seq;
    CREATE TABLE IF NOT EXISTS brand(
        brand_id INT PRIMARY KEY DEFAULT nextval('brand_id_seq'),
        brand_name TEXT NOT NULL
    );
    ALTER SEQUENCE brand_id_seq OWNED BY brand.brand_id;
    """

CREATE_PRODUCT_TABLE = \
    """
    CREATE SEQUENCE product_id_seq;
    CREATE TABLE IF NOT EXISTS product(
        product_id INT PRIMARY KEY DEFAULT nextval('product_id_seq'),
        product_name TEXT NOT NULL,
        brand_id INT NOT NULL,
        FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
    );
    ALTER SEQUENCE product_id_seq OWNED BY product.product_id;
    """

CREATE_PRODUCT_COLOR_TABLE = \
    """
    CREATE SEQUENCE product_color_id_seq;
    CREATE TABLE IF NOT EXISTS product_color(
        product_color_id INT PRIMARY KEY DEFAULT nextval('product_color_id_seq'),
        product_color_name TEXT NOT NULL
    );
    ALTER SEQUENCE product_color_id_seq OWNED BY product_color.product_color_id;
    """

CREATE_PRODUCT_SIZE_TABLE = \
    """
    CREATE SEQUENCE product_size_id_seq;
    CREATE TABLE IF NOT EXISTS product_size(
        product_size_id INT PRIMARY KEY DEFAULT nextval('product_size_id_seq'),
        product_size_name TEXT NOT NULL
    );
    ALTER SEQUENCE product_size_id_seq OWNED BY product_size.product_size_id;
    """

CREATE_SKU_TABLE = \
    """
    CREATE SEQUENCE sku_id_seq;
    CREATE TABLE IF NOT EXISTS sku(
        sku_id INT PRIMARY KEY DEFAULT nextval('sku_id_seq'),
        product_id INT NOT NULL,
        product_size_id INT NOT NULL,
        product_color_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product(product_id),
        FOREIGN KEY (product_size_id) REFERENCES product_size(product_size_id),
        FOREIGN KEY (product_color_id) REFERENCES product_color(product_color_id)
    );
    ALTER SEQUENCE sku_id_seq OWNED BY sku.sku_id
    """

COLOR_INSERT = \
    """
    INSERT INTO product_color VALUES(1, 'Blue');
    INSERT INTO product_color VALUES(2, 'Black');
    """

SIZE_INSERT = \
    """
    INSERT INTO product_size VALUES(1, 'Small');
    INSERT INTO product_size VALUES(2, 'Medium');
    INSERT INTO product_size VALUES(3, 'Large');
    """

product_query = \
    """
    SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100;
    """
