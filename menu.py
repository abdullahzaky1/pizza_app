# 1. Importing extensions
import streamlit as st
import pandas as pd

# 2. Check Authentication
if not st.session_state.get('logged_in', False):
    st.warning('⚠️ Please sign in from the navbar to access the menu!')
    st.stop()

# 3. Main menu interface   
st.title('Welcome to PizzaHub🍕', text_alignment='center')
st.success(f'Hello {st.session_state.get("name", "Customer")}, choose your order!')

# Adding menu items with prices
menu_pizza = {
    'Chicken': {'Small': 180, 'Medium': 250, 'Large': 320},
    'Margerita': {'Small': 150, 'Medium': 210, 'Large': 270}, 
    'Pepperoni': {'Small': 200, 'Medium': 280, 'Large': 350},
    'Burger': {'Small': 220, 'Medium': 320, 'Large': 400}
}
menu_pasta = {
    'Alfredo': 180,
    'Bolognese': 200,
    'Pesto': 190
}
menu_drinks = {
    'Cola': 30,
    'Sprite': 30,
    'Orange Juice': 45,
    'Water': 15
}

pizza_tab, pasta_tab, drinks_tab = st.tabs(
    ['Italian Pizza🍕', 'Italian Pasta🍝', 'Soft Drinks🥤']
)

order_items = []

with pizza_tab:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://www.papajohnsegypt.com/images/Products/product_41_1768291346.jpg') 
        st.subheader('Chicken Pizza', text_alignment='center')
        chicken_size = st.segmented_control("Size", ["Small", "Medium", "Large"], default="Medium", key="chk_size")
        if not chicken_size: chicken_size = "Medium"
        st.write(f'Price: :red[{menu_pizza["Chicken"][chicken_size]}] EGP')
        chicken_qty = st.number_input('Choose quantity:', key='chicken', min_value=0, max_value=20, step=1)
        if chicken_qty > 0:
            order_items.append({"Item": f"Chicken Pizza ({chicken_size})", "Quantity": chicken_qty, "Price": chicken_qty * menu_pizza["Chicken"][chicken_size]})
        
        st.divider()
        
        st.image('https://www.papajohnsegypt.com/images/Products/product_114_1768291821.jpg')
        st.subheader('Burger Pizza', text_alignment='center')
        burger_size = st.segmented_control("Size", ["Small", "Medium", "Large"], default="Medium", key="brg_size")
        if not burger_size: burger_size = "Medium"
        st.write(f'Price: :red[{menu_pizza["Burger"][burger_size]}] EGP')
        burger_qty = st.number_input('Choose quantity:', key='burger', min_value=0, max_value=20, step=1)
        if burger_qty > 0:
            order_items.append({"Item": f"Burger Pizza ({burger_size})", "Quantity": burger_qty, "Price": burger_qty * menu_pizza["Burger"][burger_size]})
            
    with col2:
        st.image('https://www.papajohnsegypt.com/images/Products/product_50_1768290827.jpg') 
        st.subheader('Margerita Pizza', text_alignment='center')
        marg_size = st.segmented_control("Size", ["Small", "Medium", "Large"], default="Medium", key="mrg_size")
        if not marg_size: marg_size = "Medium"
        st.write(f'Price: :red[{menu_pizza["Margerita"][marg_size]}] EGP')
        margerita_qty = st.number_input('Choose quantity:', key='margerita', min_value=0, max_value=20, step=1)
        if margerita_qty > 0:
            order_items.append({"Item": f"Margerita Pizza ({marg_size})", "Quantity": margerita_qty, "Price": margerita_qty * menu_pizza["Margerita"][marg_size]})
    
    with col3:
        st.image('https://www.papajohnsegypt.com/images/Products/product_9_1768291533.jpg') 
        st.subheader('Pepperoni Pizza', text_alignment='center')
        pep_size = st.segmented_control("Size", ["Small", "Medium", "Large"], default="Medium", key="pep_size")
        if not pep_size: pep_size = "Medium"
        st.write(f'Price: :red[{menu_pizza["Pepperoni"][pep_size]}] EGP')
        pepperoni_qty = st.number_input('Choose quantity:', key='pepperoni', min_value=0, max_value=20, step=1)
        if pepperoni_qty > 0:
            order_items.append({"Item": f"Pepperoni Pizza ({pep_size})", "Quantity": pepperoni_qty, "Price": pepperoni_qty * menu_pizza["Pepperoni"][pep_size]})

with pasta_tab:
    st.header('Italian Pasta🍝')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Fettuccine Alfredo")
        st.write(f'Price: :red[{menu_pasta["Alfredo"]}] EGP')
        alfredo_qty = st.number_input('Choose quantity:', key='alfredo', min_value=0, max_value=20, step=1)
        if alfredo_qty > 0: order_items.append({"Item": "Fettuccine Alfredo", "Quantity": alfredo_qty, "Price": alfredo_qty * menu_pasta["Alfredo"]})
        
    with col2:
        st.image("https://images.unsplash.com/photo-1626844131082-256783844137?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Spaghetti")
        st.write(f'Price: :red[{menu_pasta["Bolognese"]}] EGP')
        bolognese_qty = st.number_input('Choose quantity:', key='bolognese', min_value=0, max_value=20, step=1)
        if bolognese_qty > 0: order_items.append({"Item": "Spaghetti Bolognese", "Quantity": bolognese_qty, "Price": bolognese_qty * menu_pasta["Bolognese"]})
        
    with col3:
        st.image("https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Pesto Penne")
        st.write(f'Price: :red[{menu_pasta["Pesto"]}] EGP')
        pesto_qty = st.number_input('Choose quantity:', key='pesto', min_value=0, max_value=20, step=1)
        if pesto_qty > 0: order_items.append({"Item": "Pesto Penne", "Quantity": pesto_qty, "Price": pesto_qty * menu_pasta["Pesto"]})

with drinks_tab:
    st.header('Soft Drinks🥤')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Cola")
        st.write(f'Price: :red[{menu_drinks["Cola"]}] EGP')
        cola_qty = st.number_input('Quantity:', key='cola', min_value=0, max_value=20, step=1)
        if cola_qty > 0: order_items.append({"Item": "Cola", "Quantity": cola_qty, "Price": cola_qty * menu_drinks["Cola"]})
        
    with col2:
        st.image("https://images.unsplash.com/photo-1680404005217-a441afdefe83?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Sprite")
        st.write(f'Price: :red[{menu_drinks["Sprite"]}] EGP')
        sprite_qty = st.number_input('Quantity:', key='sprite', min_value=0, max_value=20, step=1)
        if sprite_qty > 0: order_items.append({"Item": "Sprite", "Quantity": sprite_qty, "Price": sprite_qty * menu_drinks["Sprite"]})
        
    with col3:
        st.image("https://images.unsplash.com/photo-1613478223719-2ab802602423?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Orange Juice")
        st.write(f'Price: :red[{menu_drinks["Orange Juice"]}] EGP')
        orj_qty = st.number_input('Quantity:', key='orj', min_value=0, max_value=20, step=1)
        if orj_qty > 0: order_items.append({"Item": "Orange Juice", "Quantity": orj_qty, "Price": orj_qty * menu_drinks["Orange Juice"]})
        
    with col4:
        st.image("https://images.unsplash.com/photo-1550505095-81378a674395?w=600&h=450&fit=crop", use_container_width=True)
        st.subheader("Water")
        st.write(f'Price: :red[{menu_drinks["Water"]}] EGP')
        water_qty = st.number_input('Quantity:', key='water', min_value=0, max_value=20, step=1)
        if water_qty > 0: order_items.append({"Item": "Water", "Quantity": water_qty, "Price": water_qty * menu_drinks["Water"]})

st.divider()

# Order Summary Section
st.subheader("🛒 Order Summary")

total_price = sum([item["Price"] for item in order_items])

if len(order_items) > 0:
    df = pd.DataFrame(order_items)
    
    # Clean visual for table by making index hidden or just writing using st.dataframe
    st.table(df)
    st.subheader(f'💰 Grand Total: :red[{total_price}] EGP')
else:
    st.info("Your cart is currently empty. Add items from the tabs above.")
    st.subheader(f'💰 Grand Total: :red[0] EGP')

if st.button("Place Order", use_container_width=True, type="primary"):
    if total_price > 0:
        st.success("🎉 Order placed successfully! Thank you for ordering from PizzaHub!")
    else:
        st.error("Cannot place an empty order.")
