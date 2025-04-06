import streamlit as st

def convert(value, from_unit, to_unit):
    
    length = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'inch': 0.0254,
        'foot': 0.3048,
        'mile': 1609.344
    }
    
    
    weight = {
        'mg': 0.001,
        'g': 1.0,
        'kg': 1000.0,
        'pound': 453.592,
        'ounce': 28.3495
    }
    
   
    if from_unit == '°C' and to_unit == '°F':
        return value * 9/5 + 32
    elif from_unit == '°F' and to_unit == '°C':
        return (value - 32) * 5/9
    elif from_unit in ['°C', '°F', 'K'] and to_unit in ['°C', '°F', 'K']:
       
        if from_unit == 'K' and to_unit == '°C':
            return value - 273.15
        elif from_unit == '°C' and to_unit == 'K':
            return value + 273.15
        elif from_unit == 'K' and to_unit == '°F':
            return (value - 273.15) * 9/5 + 32
        elif from_unit == '°F' and to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    
    
    if from_unit in length and to_unit in length:
        return value * length[from_unit] / length[to_unit]
    elif from_unit in weight and to_unit in weight:
        return value * weight[from_unit] / weight[to_unit]
    
    return value 

def main():
    st.title("🔢❤️ Simple Unit Converter")
    st.write("Quick conversions for everyday use")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        value = st.number_input("Enter value", value=1.0)
    
    with col2:
        unit_types = ['Length', 'Weight', 'Temperature']
        unit_type = st.selectbox("Select unit type", unit_types)
    
    with col3:
        if unit_type == 'Length':
            units = ['mm', 'cm', 'm', 'km', 'inch', 'foot', 'mile']
        elif unit_type == 'Weight':
            units = ['mg', 'g', 'kg', 'pound', 'ounce']
        else:
            units = ['°C', '°F', 'K']
        
        from_unit = st.selectbox("From", units)
    
    to_unit = st.selectbox("To", [u for u in units if u != from_unit])
    
    result = convert(value, from_unit, to_unit)
    
    st.success(f"**Result:** {value:.2f} {from_unit} = {result:.2f} {to_unit}")
    
    st.markdown("---")
    st.caption("Made with 🔢❤️ using Streamlit")

if __name__ == "__main__":
    main()