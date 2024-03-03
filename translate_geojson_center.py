import json
# 安装 ： pip install geojson
from geojson import Point, Feature, FeatureCollection

def calculate_center(feature):
    # 计算要素的中心点
    if feature['geometry']['type'] == 'Point':
        return feature['geometry']['coordinates']
    elif feature['geometry']['type'] in ['Polygon', 'MultiPolygon']:
        coords = feature['geometry']['coordinates']
        total_points = 0
        x_sum = 0
        y_sum = 0
        for polygon in coords:
            for ring in polygon:
                for point in ring:
                    total_points += 1
                    x_sum += point[0]
                    y_sum += point[1]
        return [x_sum / total_points, y_sum / total_points]
    else:
        return None

def translate_feature(feature, dx, dy):
    # 平移要素
    if feature['geometry']['type'] == 'Point':
        x, y = feature['geometry']['coordinates']
        feature['geometry']['coordinates']= [x + dx, y + dy]
    elif feature['geometry']['type'] in ['Polygon', 'MultiPolygon']:
        coords = feature['geometry']['coordinates']
        for i in range(len(coords)):
            if feature['geometry']['type'] == 'Polygon':
                coords[i] = [[x + dx, y + dy] for x, y in coords[i]]
            elif feature['geometry']['type']== 'MultiPolygon':
                coords[i] = [[[x + dx, y + dy] for x, y in ring] for ring in coords[i]]

def translate_geojson(input_file, output_file, dx, dy):
    # 读取 GeoJSON 文件，平移所有要素，然后保存结果到新的 GeoJSON 文件中
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    features = data['features']
    
    for feature in features:
        translate_feature(feature, dx, dy)
    
    with open(output_file, 'w') as f:
        json.dump(data, f)

# 输入文件
input_file = 'input.geojson'
# 输出文件
output_file = 'output.geojson'
# 偏移量
dx = -1.0545  # 在x方向平移的距离  
dy = 2.8305  # 在y方向平移的距离

translate_geojson(input_file, output_file, dx, dy)
