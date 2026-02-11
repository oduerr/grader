You are to implement a single-file web application (grader_enter.html) for fast, low-error exam grade entry. Which should produce tsp-files for the app given in index.html. An example is given the test-data/test_grading_data.txt.

⸻

Technical Constraints
	•	Deliver exactly one file: index.html
	•	All CSS and JavaScript must be inline
	•	Client-side only (no backend)
	•	No frameworks required (vanilla JS preferred)
	•	Target browsers: Chrome and Firefox only
	•	Safari is explicitly out of scope

⸻

Initial Setup Behavior

When the app starts:
	•	If the user does not import a TSV file, the app must prompt the user to:
	•	Enter the number of tasks
	•	Optionally auto-generate labels (A1, A2, A3, …)
	•	If the user imports a TSV file, task names must be:
	•	Inferred from the header
	•	Used as the active task configuration

The app must always know how many tasks exist before starting input.

⸻

Core Input Workflow (Stepper)

Step-by-step input:
	1.	Enter matriculation number
	2.	Enter task scores sequentially
	3.	After last task → automatically switch to Review
	4.	Review screen
	5.	Confirm or Correct

After confirmation:
	•	Record is saved
	•	Automatically return to matriculation number input

Must work:
	•	Without mouse (keyboard-only on laptop)
	•	Without small system keyboard (virtual keypad on touch)

⸻

Input Methods

Touch Devices

Provide a large on-screen numeric keypad:
	•	Digits 0–9
	•	Decimal point .
	•	Backspace
	•	Clear
	•	Enter / Next

All numeric input must be possible via this keypad.

Laptop Keyboard Mode

Global key bindings:
	•	Enter → next / confirm
	•	Backspace → delete
	•	Esc → go back
	•	Ctrl+Z / Cmd+Z → undo last saved record

A small visible keyboard hint panel must be shown in desktop mode, e.g.:
Enter = Next
Backspace = Delete
Esc = Back
Ctrl+Z = Undo last entry


Text-to-Speech (Chrome/Firefox Only)

Default Behavior
	•	Text-to-Speech must be enabled by default
	•	There must be a clearly visible toggle control on the page:
	•	Checkbox or button labeled e.g. “Read entries aloud”
	•	The user must be able to disable it at any time

When to Read

After the last task value is entered:
	•	Automatically switch to Review
	•	Automatically read the entire record aloud (if enabled)

What to Read

Example structure:

“Matriculation number 312046.
A1: 9. A2: 8. A3: 2. A4: 2.
Please confirm.”

Controls
	•	A Replay button must be available on the Review screen
	•	Speech must be cancelled immediately if:
	•	User presses Correct
	•	User navigates back
	•	User disables TTS

Implementation must use:
	•	Web Speech API (speechSynthesis)
	•	No Safari compatibility required

⸻

Review Screen

Must clearly display:
	•	Matriculation number
	•	All task values
	•	Optional total

Buttons:
	•	OK / Save
	•	Correct / Back
	•	Replay (for speech)

⸻

TSV Import

Button: Load TSV

Behavior:
	•	Parse header
	•	Infer tasks
	•	Load all records
	•	Ignore empty trailing lines
	•	After import, new entries are appended

Must handle errors:
	•	Missing header
	•	Invalid numeric values
	•	Column mismatch

⸻

TSV Export

Button: Export TSV

Must provide:
	•	Download as grades.tsv
	•	Copy TSV to clipboard

Must include:
	•	Header
	•	All records

⸻

Duplicate Handling

If a matriculation number already exists:

Show dialog with options:
	•	Overwrite existing
	•	Duplicate (add another row)
	•	Cancel

⸻

Validation
	•	Matriculation number must not be empty
	•	Points must be numeric
	•	Optional: enforce 0.5 step size
	•	Saving must be blocked on invalid input

⸻

UI / UX Requirements
	•	Large, high-contrast buttons
	•	Clear step indicator:
“Step 3 / 6 – Task A2”
	•	Calm, readable review screen
	•	Responsive layout
	•	Optimized for fast repetitive entry

⸻

Deliverable

One working file: index.html

No additional files.
No backend.
Chrome and Firefox only.