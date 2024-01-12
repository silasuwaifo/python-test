import psycopg2
from bs4 import BeautifulSoup
from collections import Counter

# Corrected HTML content
html_content = '''
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# 1. Which color of shirt is the mean color?
colors = [color.strip() for color in soup.find_all('tr')[1].find('td').text.split(',')]
mean_color = max(set(colors), key=colors.count)
print(f"Mean Color: {mean_color}")

# 2. Which color is mostly worn throughout the week?
all_colors = [color.strip() for color in soup.find_all('td')[1].text.split(',')]
most_common_color = Counter(all_colors).most_common(1)[0][0]
print(f"Most Common Color: {most_common_color}")

# 3. Which color is the median?
median_color = sorted(all_colors, key=all_colors.count, reverse=True)[len(all_colors) // 2]
print(f"Median Color: {median_color}")

# 4. Get the variance of the colors
color_counts = Counter(all_colors)
total_colors = len(all_colors)
variance = sum((color_counts[color] - (total_colors / len(color_counts)) ** 2) ** 2 for color in color_counts) / total_colors
print(f"Variance of Colors: {variance:.2f}")

# 5. What is the probability that the color is red?
red_count = color_counts.get('RED', 0)
probability_red = red_count / total_colors
print(f"Probability of Red: {probability_red:.2f}")

# 6. Save the colors and their frequencies in a PostgreSQL database
conn = psycopg2.connect(
    database="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

# Create a table to store colors and their frequencies
cur.execute("CREATE TABLE IF NOT EXISTS color_frequencies (color text, frequency integer);")

# Insert color frequencies into the database
for color, count in color_counts.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s);", (color, count))

conn.commit()
conn.close()

# 7. Write a recursive searching algorithm to search for a number entered by the user in a list of numbers
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1  # Number not found
    if numbers[index] == target:
        return index  # Number found
    return recursive_search(numbers, target, index + 1)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example list of numbers
target_number = int(input("Enter a number to search for: "))
result = recursive_search(numbers_list, target_number)

if result != -1:
    print(f"Number {target_number} found at index {result}.")
else:
    print(f"Number {target_number} not found in the list.")
