## 1. Python Naming Rules (Strict)

These are enforced by the Python interpreter. If you break these rules, your code will fail with a `SyntaxError`.

* **Allowed Characters:** Names can only contain alphanumeric characters (`A-Z`, `a-z`, `0-9`) and underscores (`_`).
* **Cannot Start with a Number:** A variable name can start with a letter or an underscore, but **never** a number (e.g., `1variable` is invalid).
* **Case-Sensitivity:** Python is case-sensitive. `age`, `Age`, and `AGE` are three completely different variables.
* **No Reserved Keywords:** You cannot use words that Python reserves for its own logic, such as `if`, `else`, `while`, `for`, `class`, or `import`.

### Examples of Valid vs. Invalid Names

| Valid Names | Invalid Names | Reason for Failure |
   |
| `user_age` | `user-age` | Hyphens are not allowed. |
| `_temp` | `1st_place` | Cannot start with a number. |
| `total2` | `total$` | Special characters (`$`) are not allowed. |
| `is_active` | `class` | `class` is a reserved Python keyword. |

## 2. Popular Naming Conventions (PEP 8)

Conventions are stylistic guidelines followed by the Python community to keep code uniform and readable. Most of these come directly from **PEP 8**, the official Python style guide.

The four most common casing styles used in Python are:

* **`snake_case`**: Words are lowercase and separated by underscores.
* **`PascalCase`** (or **`CamelCase`**): Every word starts with a capital letter, with no spaces.
* **`UPPERCASE_SNAKE_CASE`**: All letters are capitalized, with words separated by underscores.

### Python Naming Conventions by Object Type

| Object Type | Convention | Example |
   |
| **Variables** | `snake_case` | `total_price`, `user_id` |
| **Functions & Methods** | `snake_case` | `calculate_total()`, `get_data()` |
| **Classes** | `PascalCase` | `UserProfile`, `ShoppingCart` |
| **Constants** | `UPPER_CASE_SNAKE` | `PI`, `MAX_CONNECTIONS`, `API_URL` |
| **Modules & Packages** | Short, lowercase, no underscores if possible | `math`, `requests`, `json` |

## 3. The Meaning of Underscores

Underscores have special meanings in Python naming conventions, signaling intent to other developers:

* **Single Leading Underscore (`_variable`):** A gentle warning to other programmers that a variable or method is intended for **internal use** (private) within a class or module. Python won't stop you from accessing it, but it's a polite "please don't touch this."
* **Single Trailing Underscore (`class_`):** Used by convention to avoid conflicts with Python keywords. If you absolutely need a variable named "class", you write `class_`.
* **Double Leading Underscore (`__variable`):** Triggers **name mangling**, where Python physically changes the variable name behind the scenes to prevent it from being accidentally overwritten in subclasses.
* **Dunder (Double Under) (`__init__`):** Reserved for special, built-in system methods (like constructors or operators). You should never invent your own dunder names; only use the ones Python provides.


## Difference With Other Languages

While Python heavily favors `snake_case` and `PascalCase`, other programming languages have developed their own distinct stylistic standards based on their syntax, community history, and corporate origins.

Here is how naming conventions shake out across the rest of the programming world.

## 1. JavaScript & TypeScript

The web ecosystem relies almost entirely on **camelCase** for standard logic and **PascalCase** for object-oriented structures.

* **Variables & Functions:** `camelCase` (e.g., `totalPrice`, `fetchUserData()`).
* **Classes & Interfaces:** `PascalCase` (e.g., `UserSession`, `AuthRepository`).
* **Constants:** `UPPERCASE_SNAKE_CASE` (e.g., `MAX_RETRY_ATTEMPTS`).
* **Private Properties:** Modern JavaScript uses a physical `#` prefix (`#internalId`) enforced by the engine, though older code bases use a single leading underscore (`_internalId`).

## 2. Java

Java's ecosystem is incredibly strict about its conventions. Nearly all Java code in the wild looks identical structurally.

* **Variables & Methods:** `camelCase` (e.g., `employeeSalary`, `calculateTax()`).
* **Classes & Interfaces:** `PascalCase` (e.g., `DatabaseConnection`, `Runnable`).
* **Constants:** `UPPERCASE_SNAKE_CASE` declared with `String final` modifiers (e.g., `DEFAULT_TIMEOUT`).
* **Packages:** Strictly lowercase, hierarchical, and usually starting with a reversed internet domain name (e.g., `com.company.project.utilities`).

## 3. C++

C++ is a unique case because it does not have a single universally accepted style guide. Conventions heavily depend on the specific framework, company, or historical era of the codebase.

* **Standard Library Style (std):** Mimics Python's `snake_case` for variables and functions (e.g., `std::vector`, `push_back()`).
* **Google C++ Style Guide:**
* Variables: `snake_case` with a trailing underscore for class member variables (e.g., `student_name_`).
* Functions: `PascalCase` (e.g., `OpenFile()`).


* **Hungarian Notation (Older/Windows legacy):** Prefixes variable names with a short abbreviation indicating its data type. While largely phased out, you will still see it in Windows API environments (e.g., `strName` for a string, `iCount` for an integer, `pPointer` for a pointer).

## 4. C#

Managed by Microsoft, C# favors capitalization over underscores. It stands out by using `PascalCase` for methods where almost every other language uses `camelCase`.

* **Methods & Classes:** `PascalCase` (e.g., `SaveConfiguration()`, `CustomerController`).
* **Local Variables:** `camelCase` (e.g., `invoiceTotal`).
* **Private Fields:** `camelCase` prefixed with an underscore (e.g., `_connectionString`).
* **Interfaces:** Explicitly prefixed with a capital `I` in `PascalCase` (e.g., `ILogger`, `IDisposable`).

## 5. Lisp, Clojure, & CSS

Many functional languages and styling sheets use a convention known as **kebab-case** (or spinal-case), where words are separated by hyphens.

```clojure
;; Clojure example (Hyphens are valid mathematical characters, not subtraction syntax here)
(defn calculate-total-price [items] ...)

```

```css
/* CSS Example */
.main-navigation-menu { ... }

```

> **Why Python/Java/C can't use kebab-case:** In those languages, a hyphen means subtraction. Writing `total-price` would make the compiler think you are trying to subtract `price` from `total`.

## Quick Reference Summary

| Language         | Variables    | Functions / Methods | Classes      | Constants                    |
| -- | -- | -- | -- | -- |
| **Python**       | `snake_case` | `snake_case`        | `PascalCase` | `UPPER_SNAKE`                |
| **JavaScript**   | `camelCase`  | `camelCase`         | `PascalCase` | `UPPER_SNAKE`                |
| **Java**         | `camelCase`  | `camelCase`         | `PascalCase` | `UPPER_SNAKE`                |
| **C#**           | `camelCase`  | `PascalCase`        | `PascalCase` | `PascalCase` / `UPPER_SNAKE` |
| **C++ (Google)** | `snake_case` | `PascalCase`        | `PascalCase` | `kConstantName`              |