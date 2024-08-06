
def keep_descriptions(input_filename, output_filename):
    # lineKeywords that indicate non-description lines
    lineKeywords = ['Wetland', 'Soil:', 'Form/Color', 'Stormwater', 'Urban', 'Habitat:', 
                'Ecosystem', 'Hydrology:','Salt', 'Other:', 'Shade', 
                'Tolerance:', 'Indicator:', 'Services:','Value:', 'Page']
    
    singleKeywords = ['Horticultural','Compatibility:']
    
    
    
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            line = line.strip()
            
            if any(line.startswith(keyword) for keyword in singleKeywords) and line:
                for keyword in singleKeywords:
                        line = line.replace(keyword, '').strip()
            if not any(line.startswith(keyword) for keyword in lineKeywords) and line:
                 output_file.write(line + '\n')   
                 #if line is > x characters make group next line after 

# Usage
keep_descriptions('plantscrape.txt', 'output.txt')
