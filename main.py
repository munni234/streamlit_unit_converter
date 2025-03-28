#from unit 
#to unit 
#value
import streamlit as st



def height_conversion(value, from_unit, to_unit):

    conversion_factors = {
        "kilometer": 1000,
        "meter": 1,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }

    if from_unit == to_unit:
        return f"{value} {to_unit} (No conversion needed)"

    if from_unit in conversion_factors and to_unit in conversion_factors:

         res =  value * (conversion_factors[from_unit] / conversion_factors[to_unit])
         
         return f"{res} {to_unit}"
    else:
        return "Conversion is not supported"
    

def time_conversion(value, from_unit, to_unit):

    conversion_factors = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2629746,
        "year": 31556952
    }

    if from_unit == to_unit:
        return f"{value} {to_unit} (No conversion needed)"

    if from_unit in conversion_factors and to_unit in conversion_factors:
    
     res = value * (conversion_factors[from_unit] / conversion_factors[to_unit])

     return f"{res} {to_unit}"
    else:
        return "Invalid conversion"



def volume_conversion(value, from_unit, to_unit):

 conversion_factors = {
    "cubic meter": 1,             # Base unit
    "liter": 0.001,               # ✅ 1 L = 0.001 m³
    "milliliter": 0.000001,       # ✅ 1 mL = 1 cm³ = 10⁻⁶ m³
    "cubic foot": 0.0283168,      # ✅ 1 ft³ = 0.0283168 m³
    "cubic inch": 0.000016387,    # ✅ 1 in³ = 0.000016387 m³
    "liquid gallon": 0.00378541,  # ✅ 1 US gallon = 3.78541 L = 0.00378541 m³
    "imperial gallon": 0.00454609, # ✅ 1 UK gallon = 4.54609 L = 0.00454609 m³
    "teaspoon": 0.00000492892,     # ✅ 1 tsp (US) = 4.92892 cm³ = 4.92892 × 10⁻⁶ m³
    "tablespoon": 0.0000147868,   # ✅ 1 tbsp (US) = 14.7868 cm³ = 1.47868 × 10⁻⁵ m³
    "cup": 0.000236588,           # ✅ 1 US cup = 236.588 mL = 0.000236588 m³
}
 

 if from_unit == to_unit:
        return f"{value} {to_unit} (No conversion needed)"

 if from_unit in conversion_factors and to_unit in conversion_factors:
    
     res = int(value * int((conversion_factors[from_unit] / conversion_factors[to_unit])))

     return res , "volume conversion"
 else:
        return "Invalid conversion"
 

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return f"{value} {to_unit} (No conversion needed)"

    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return f"{(value * 9/5) + 32:.2f} °F"
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return f"{(value - 32) * 5/9:.2f} °C"
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return f"{value + 273.15:.2f} K"
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return f"{value - 273.15:.2f} °C"
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return f"{(value - 32) * 5/9 + 273.15:.2f} K"
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return f"{(value - 273.15) * 9/5 + 32:.2f} °F"
    else:
        return "Invalid conversion"
   
   
           

def main():
     
 st.title("Unit Converter")
 st.write("Select the category to perform conversion.")

 category = st.selectbox("Select the Category " , [ "Time", "Mass" , "Temperature" ,"Volume" ])
 value = st.number_input("Enter the value", min_value=0.0, value=1.0 )

 
 
 if category == "Time":
    from_unit =  st.selectbox("From",["second", "minute", "hour", "day", "week", "month", "year"])
    to_unit =  st.selectbox("To ",["second", "minute", "hour", "day", "week", "month", "year"])

    if st.button("Convert", key="time_conversion"):
         st.write(time_conversion(value, from_unit, to_unit))
   
 elif category == "Mass":
     from_unit =  st.selectbox("From", ["kilometer", "meter", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
     to_unit =  st.selectbox("To ", ["kilometer", "meter", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])

     if st.button("Convert", key="mass_conversion"):
          st.write(height_conversion(value, from_unit, to_unit))

     
 elif category == "Volume":
         from_unit = st.selectbox("From", ["cubic meter", "liter", "milliliter", "cubic foot", "cubic inch", "liquid gallon", "imperial gallon", "teaspoon", "tablespoon", "cup"])
         to_unit = st.selectbox("To", ["cubic meter", "liter", "milliliter", "cubic foot", "cubic inch", "liquid gallon", "imperial gallon", "teaspoon", "tablespoon", "cup"])

         if st.button("convert", key="vol_conversion"):
            st.write(volume_conversion(value, from_unit, to_unit))
          
 elif category == "Temperature":
          from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
          to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
          if st.button("Convert", key="temperature_conversion"):
            st.write(temperature_conversion(value, from_unit, to_unit))

 else:
     return "Conversion not supported"
 

 st.write("Made with  ♥♥  by 'FAIZA ABBASI'")
          


if __name__ == "__main__":
     main()

