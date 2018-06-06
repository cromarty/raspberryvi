<!-- 
.. title: Nano Editor Reference
.. slug: nano-editor-reference
.. date: 2015-05-18 12:27:35 UTC
.. tags: nano, editor, reference
.. category: Reference
.. link: 
.. description: Blind-friendly nano editor reference
.. type: text
-->


Below is a representation of the help-text displayed in the nano editor when the key combination ^G (control+G) is pressed.

I have posted this here because editing a file is obviously a very visual exercise and so warrants an entry in the Reference wiki.  Editing a file with Nano is a sufficiently different experience for a VI user either connected over <abbr title="Secure Shell">SSH</abbr> or locally.  Also because I have so far failed to learn enough commands to make Nano editing a pleasant experience.  I will surely be using this page for reference a lot and expect it will also be useful to others.

There seems to be very little online with regard to command reference for the Nano editor.  With such a useful help screen this is not surprising.  However this doesn&#039;t help the VI user accessing the editor screen with a screen-reader.  Reading the help text would involve use of flat-review and slow down editing operations dramatically.

The keystrokes list has been tabulated for ease of navigation.  Otherwise it is verbatim from the Nano help window.

Notes for VI use of Nano:

1.  The top line shows three sections.  The first is the version of the program.  The centre section is the current file being edited or &#039;new buffer&#039;.  The third section is empty until a change is made, at which time the word &#039;Modified&#039; appears here, triggering most screen-readers to say the word &#039;modified&#039;.
2.  At the bottom of the screens are three lines which are not part of the editor window.  Third from bottom is a line where helpful messages appear and where you will type search strings etc.  The bottom two lines show the most common shortcut key combinations and is pretty much inaccessible to a VI user.  So remembering the most useful keystroke combinations is vital.
3.  When in &#039;expert&#039; mode, the bottom two lines of keystroke reminders disappear and the editor window grows by two lines, putting the message line at the bottom of the screen.
4.  I&#039;ve noticed some pretty bizarre behaviour from Nano used over an <abbr title="Secure Shell">SSH</abbr> connection with Tera-Term.  Including some lines being read twice, and sometimes some blank lines appearing at the beginning of the file where there weren&#039;t any before.  Some of this behaviour may be my host screen-reader, some may not be.
5.  The help suggests using the &#039;Alt&#039; key for the &#039;Meta&#039; character.  Obviously this is out of the question when accessing the Pi over an <abbr title="Secure Shell">SSH</abbr> connection from a Windows host as in most terminal applications, and most Windows applications of any kind, the &#039;Alt&#039; key will open the terminal program menu and the keystroke will not be passed to Nano.

The help text verbatim:

Main Nano help Text

The Nano editor is designed to emulate the ease-of-use of the UW Pico text editor.  There are four main sections of the editor.  The top line shows the version of the program, the current filename being edited, and whether or not the file has been modified. Next is the main editor window showing the file being editied. The status line is the third line from the bottom and shows important messages. The bottom two lines show the most commonly used shortcuts.

The notation for shortcuts is as follows: Control-key sequences are notated with a caret (^) symbol and can be entered either by entering the control (Ctrl) key or by pressing the escape (Esc) key twice.  Escape-key sequences are notated with the Meta (M-) symbol and can be entered by pressing either the Esc, Alt or Meta key, depending on the setup of your keyboard.  Also, pressing the Esc key twice followed by a three-digit decimal number from 000 to 255 will enter the character with the corresponding value. 

The following keystrokes are available in the main editor window.  Alternative keys are shown in parentheses:


<table class="inline">
	<tr class="row0">
		<th class="col0 centeralign">  Key Combo  </th><th class="col1 centeralign">  Function  </th>
	</tr>
	<tr class="row1">
		<td class="col0 centeralign">  ^G (F1)  </td><td class="col1 leftalign"> Display the help text   </td>
	</tr>
	<tr class="row2">
		<td class="col0 centeralign">  ^Y  </td><td class="col1 leftalign"> Go up one screen in help text  </td>
	</tr>
	<tr class="row3">
		<td class="col0 centeralign">  ^V  </td><td class="col1 leftalign"> Go down one line in help text  </td>
	</tr>
	<tr class="row4">
		<td class="col0 centeralign">  ^X (F2)  </td><td class="col1 leftalign"> Exit the help text  </td>
	</tr>
	<tr class="row5">
		<td class="col0 centeralign">  ^O (F3)  </td><td class="col1 leftalign"> Save the current buffer  </td>
	</tr>
	<tr class="row6">
		<td class="col0 centeralign">  ^J (F4)  </td><td class="col1 leftalign"> Justify the current paragraph  </td>
	</tr>
	<tr class="row7">
		<td class="col0 leftalign"> ^R (F5)  </td><td class="col1 leftalign"> Insert another file into current file  </td>
	</tr>
	<tr class="row8">
		<td class="col0 centeralign">  ^W (F6)  </td><td class="col1 leftalign"> Search for a string  </td>
	</tr>
	<tr class="row9">
		<td class="col0 centeralign">  ^Y (F7)  </td><td class="col1 leftalign"> Go to previous screen of buffer  </td>
	</tr>
	<tr class="row10">
		<td class="col0 centeralign">  ^V (F8)  </td><td class="col1 leftalign"> Go to next screen of current buffer  </td>
	</tr>
	<tr class="row11">
		<td class="col0 centeralign">  ^K  </td><td class="col1 leftalign"> Cut the current line to the cut buffer (try saying that quickly)  </td>
	</tr>
	<tr class="row12">
		<td class="col0 centeralign">  ^U  </td><td class="col1 leftalign"> Paste from the cut buffer into the current buffer (at cursor position)  </td>
	</tr>
	<tr class="row13">
		<td class="col0 centeralign">  ^C (F11)  </td><td class="col1 leftalign"> Display the position of the current cursor  </td>
	</tr>
	<tr class="row14">
		<td class="col0 centeralign">  ^T  </td><td class="col1 leftalign"> Invoke the spell-checker (if available)  </td>
	</tr>
	<tr class="row15">
		<td class="col0 centeralign">  M-\  </td><td class="col1 leftalign"> Go to first line of current buffer  </td>
	</tr>
	<tr class="row16">
		<td class="col0 centeralign">  M-/  </td><td class="col1 leftalign"> Go to last line of current buffer  </td>
	</tr>
	<tr class="row17">
		<td class="col0 rightalign">  ^_ (M-G) </td><td class="col1 leftalign"> Go to line number  </td>
	</tr>
	<tr class="row18">
		<td class="col0 centeralign">  ^\ (M-R)  </td><td class="col1 leftalign"> Replace string or regular expression  </td>
	</tr>
	<tr class="row19">
		<td class="col0 centeralign">  ^^ (M-A)  </td><td class="col1 leftalign"> Mark at current position  </td>
	</tr>
	<tr class="row20">
		<td class="col0 centeralign">  M-W  </td><td class="col1 leftalign"> Repeat last search  </td>
	</tr>
	<tr class="row21">
		<td class="col0 centeralign">  M-^ (M-6)  </td><td class="col1 leftalign"> Copy current line to cut buffer without removing it  </td>
	</tr>
	<tr class="row22">
		<td class="col0 centeralign">  M-}  </td><td class="col1 leftalign"> Indent current line  </td>
	</tr>
	<tr class="row23">
		<td class="col0 centeralign">  M-{  </td><td class="col1 leftalign"> Outdent current line  </td>
	</tr>
	<tr class="row24">
		<td class="col0 centeralign">  ^F  </td><td class="col1 leftalign"> Forward one character  </td>
	</tr>
	<tr class="row25">
		<td class="col0 centeralign">  ^B  </td><td class="col1 leftalign"> Backward one character  </td>
	</tr>
	<tr class="row26">
		<td class="col0 centeralign">  ^&lt;spacebar&gt;  </td><td class="col1 leftalign"> Forward one word  </td>
	</tr>
	<tr class="row27">
		<td class="col0 centeralign">  M-&lt;spacebar&gt;  </td><td class="col1 leftalign"> Backward one word  </td>
	</tr>
	<tr class="row28">
		<td class="col0 leftalign"> ^P  </td><td class="col1 leftalign"> Previous line  </td>
	</tr>
	<tr class="row29">
		<td class="col0 centeralign">  ^N  </td><td class="col1 leftalign"> Next line  </td>
	</tr>
	<tr class="row30">
		<td class="col0 centeralign">  ^A  </td><td class="col1 leftalign"> Beginning of current line  </td>
	</tr>
	<tr class="row31">
		<td class="col0 centeralign">  ^E  </td><td class="col1 leftalign"> End of current line  </td>
	</tr>
	<tr class="row32">
		<td class="col0 leftalign"> M-( (M-9)  </td><td class="col1 leftalign"> Go to beginning of current paragraph; then back to beginning of subsequent paragraphs for each repeated operation  </td>
	</tr>
	<tr class="row33">
		<td class="col0 centeralign">  M-) (M-0)  </td><td class="col1 leftalign"> Go to position before next paragraph; and then forward by paragraph for each repeated operation  </td>
	</tr>
	<tr class="row34">
		<td class="col0 centeralign">  M-]  </td><td class="col1 leftalign"> Go to matching bracket  </td>
	</tr>
	<tr class="row35">
		<td class="col0 centeralign">  ^M  </td><td class="col1 leftalign"> Insert a newline at the current cursor position  </td>
	</tr>
	<tr class="row36">
		<td class="col0 centeralign">  ^D  </td><td class="col1 leftalign"> Delete the character under the cursor (to the right of vertical bar cursor)  </td>
	</tr>
	<tr class="row37">
		<td class="col0 centeralign">  ^H  </td><td class="col1 leftalign"> Delete the character to the left of the cursor  </td>
	</tr>
	<tr class="row38">
		<td class="col0 centeralign">  M-T  </td><td class="col1 leftalign"> Cut buffer from current cursor position to end  </td>
	</tr>
	<tr class="row39">
		<td class="col0 centeralign">  M-J  </td><td class="col1 leftalign"> Justify entire buffer  </td>
	</tr>
	<tr class="row40">
		<td class="col0 centeralign">  M-D  </td><td class="col1 leftalign"> Count the number of words, lines and characters in the buffer  </td>
	</tr>
	<tr class="row41">
		<td class="col0 centeralign">  ^L  </td><td class="col1 leftalign"> Redraw the current screen  </td>
	</tr>
	<tr class="row42">
		<td class="col0 centeralign">  ^Z  </td><td class="col1 leftalign"> Suspend the editor, if suspending is enabled  </td>
	</tr>
	<tr class="row43">
		<td class="col0 centeralign">  M-X  </td><td class="col1 leftalign"> Help mode enable/disable  </td>
	</tr>
	<tr class="row44">
		<td class="col0 centeralign">  M-C  </td><td class="col1 leftalign"> Constant cursor mode enable/disable  </td>
	</tr>
	<tr class="row45">
		<td class="col0 centeralign">  M-O  </td><td class="col1 leftalign"> Use of one more line for editing enable/disable  </td>
	</tr>
	<tr class="row46">
		<td class="col0 centeralign">  M-F  </td><td class="col1 leftalign"> Move scrolling enable/disable  </td>
	</tr>
	<tr class="row47">
		<td class="col0 centeralign">  M-P  </td><td class="col1 leftalign"> Whitespace display enable/disable  </td>
	</tr>
	<tr class="row48">
		<td class="col0 centeralign">  M-Y  </td><td class="col1 leftalign"> Colour syntax highlighting enable/disable  </td>
	</tr>
	<tr class="row49">
		<td class="col0 centeralign">  M-H  </td><td class="col1 leftalign"> Smart home key enable/disable  </td>
	</tr>
	<tr class="row50">
		<td class="col0 centeralign">  M-I  </td><td class="col1 leftalign"> Auto-indent enable/disable  </td>
	</tr>
	<tr class="row51">
		<td class="col0 centeralign">  M-K  </td><td class="col1 leftalign"> Cut to end enable/disable  </td>
	</tr>
	<tr class="row52">
		<td class="col0 centeralign">  M--  </td><td class="col1 leftalign"> Scroll back one line without moving the cursor  </td>
	</tr>
	<tr class="row53">
		<td class="col0 centeralign">  M-+  </td><td class="col1 leftalign"> Scroll forward one line without moving the cursor  </td>
	</tr>
	<tr class="row54">
		<td class="col0 centeralign">  M-&lt;  </td><td class="col1 leftalign"> Switch to the previous buffer  </td>
	</tr>
	<tr class="row55">
		<td class="col0 centeralign">  M-&gt;  </td><td class="col1 leftalign"> Switch to the next buffer  </td>
	</tr>
	<tr class="row56">
		<td class="col0 centeralign">  M-V  </td><td class="col1 leftalign"> Insert the next keystroke verbatim  </td>
	</tr>
	<tr class="row57">
		<td class="col0 centeralign">  ^I  </td><td class="col1 leftalign"> Insert a tab at the current cursor position  </td>
	</tr>
	<tr class="row58">
		<td class="col0 centeralign">  M-L  </td><td class="col1 leftalign"> Long line wrap enable/disable  </td>
	</tr>
	<tr class="row59">
		<td class="col0 centeralign">  M-Q  </td><td class="col1 leftalign"> Conversion of typed tabs to spaces enable/disable  </td>
	</tr>
	<tr class="row60">
		<td class="col0 centeralign">  M-B  </td><td class="col1 leftalign"> Backup files enable/disable  </td>
	</tr>
	<tr class="row61">
		<td class="col0 centeralign">  M-F  </td><td class="col1 leftalign"> Multiple file buffers enable/disable  </td>
	</tr>
	<tr class="row62">
		<td class="col0 centeralign">  M-M  </td><td class="col1 leftalign"> Mouse support enable/disable  </td>
	</tr>
	<tr class="row63">
		<td class="col0 centeralign">  M-N  </td><td class="col1 leftalign"> No conversion from DOS/Mac format enable/disable  </td>
	</tr>
	<tr class="row64">
		<td class="col0 centeralign">  M-Z  </td><td class="col1 leftalign"> Editor suspension enable/disable  </td>
	</tr>
	<tr class="row65">
		<td class="col0 centeralign">  M-$  </td><td class="col1 leftalign"> Soft-line wrapping enable/disable  </td>
	</tr>
</table>


