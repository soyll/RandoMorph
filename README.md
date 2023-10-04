<img src="https://github.com/soyll/RandoMorph/blob/main/logo.gif" data-canonical-src="https://github.com/soyll/RandoMorph/blob/main/logo.gif" width="1000" height="550" />

# RandoMorph
The **RandoMorph** is a simple Python library designed for generating random data of various types, including strings, names, addresses, numbers, and more. This library is ideal for creating test data, mock-ups, or demonstration samples.

## Table of Contents
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
  * [Result](#result)
* [**Arguments**](#arguments)
* [Plans](#plans)
## Getting Started

### Installation
#### Install using pypi
```bash
pip install randomorph
```
or
* Clone the GitHub repository:
	```bash
	git clone https://github.com/soyll/RandoMorph.git	
	```
* Navigate to directory:
	```bash
	cd RandoMorph	
	```
* (Recommended) Create a virtual environment to manage Python packages for your project:
	```bash
	python3 -m venv venv
	```
* Activate the virtual enviropment
	* On windows:
		```bash
		.\venv\Scripts\activate
		```  
	* On linux or macOs:
		```
		source venv/bin/activate
		```
* Install the required Python packages from  `requirements.txt`:
	```bash
	pip install -r requirments.txt
	```
## Usage

```python
from RandoMorph import test  
  
example = test.randoMorph()  
  
example.generate(sample="Address Email Name", length=5, file_name="test.png", output_path="")
```

## Result

![](https://github.com/soyll/RandoMorph/blob/main/test.png)

## Arguments
| Argument Name | Description | Conditions | Example |
| --- | --- | --- | --- |
| `sample` | Examples of data that should be included in the file. Can include addresses, dates, email addresses, user IDs, and names. Multiple options can be specified in any order. | Options: `Address`, `Date`, `Email`, `User_id`, `Name`. Multiple options can be used in different combinations. | `sample='Name' 'Email'` |
| `length` | The length of the table, i.e., the number of rows in the generated file. Limited to values less than 100. | Integer `1<N<100`. | `length=50` |
| `filename` | The name of the file and its extension in which the result will be saved. | A string with a valid file extension (e.g., 'xlsx', 'png', 'json', 'csv'). | `filename='sample_data.xlsx'` |
| `output_path` | The path where the file will be saved. | A string representing the directory path where the file should be saved. | `output_path='/path/to/save/'` |

## Plans
* Expand dictionaries to 1,000 units
* Rework the code so that it automatically detects new dictionaries and processes them.
* Add more file types to support 
