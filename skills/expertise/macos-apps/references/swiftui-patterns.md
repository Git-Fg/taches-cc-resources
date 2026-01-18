### Overview
Modern SwiftUI patterns for macOS apps. Covers @Bindable usage, navigation (NavigationSplitView, NavigationStack), windows, toolbars, menus, lists/tables, forms, sheets/alerts, drag & drop, focus management, and keyboard shortcuts.

### Sections
Reference sections:
- observation_rules - @Bindable, @Observable, environment patterns
- navigation - NavigationSplitView, NavigationStack, drill-down
- windows - WindowGroup, Settings, auxiliary windows
- toolbar - Toolbar items, customizable toolbars
- menus - App commands, context menus
- lists_and_tables - List selection, Table, OutlineGroup
- forms - Settings forms, validation
- sheets_and_alerts - Sheets, confirmation dialogs, file dialogs
- drag_and_drop - Draggable items, drop targets, reorderable lists
- focus_and_keyboard - Focus state, keyboard shortcuts
- previews - Preview patterns

### Observation Rules
#### Passing Model Objects
**Critical rule for SwiftData @Model objects**: Use `@Bindable` when the child view needs to observe property changes or create bindings. Use `let` only for static display.

```swift
// CORRECT: Use @Bindable when observing changes or binding
struct CardView: View {
    @Bindable var card: Card  // Use this for @Model objects

    var body: some View {
        VStack {
            TextField("Title", text: $card.title)  // Binding works
            Text(card.description)  // Observes changes
        }
    }
}

// WRONG: Using let breaks observation
struct CardViewBroken: View {
    let card: Card  // Won't observe property changes!

    var body: some View {
        Text(card.title)  // May not update when card.title changes
    }
}
```

#### When To Use Bindable
**Use `@Bindable` when:**
- Passing @Model objects to child views that observe changes
- Creating bindings to model properties ($model.property)
- The view should update when model properties change

**Use `let` when:**
- Passing simple value types (structs, enums)
- The view only needs the value at the moment of creation
- You explicitly don't want reactivity

```swift
// @Model objects - use @Bindable
struct ColumnView: View {
    @Bindable var column: Column  // SwiftData model

    var body: some View {
        VStack {
            Text(column.name)  // Updates when column.name changes
            ForEach(column.cards) { card in
                CardView(card: card)  // Pass model, use @Bindable in CardView
            }
        }
    }
}

// Value types - use let
struct BadgeView: View {
    let count: Int  // Value type, let is fine

    var body: some View {
        Text("\(count)")
    }
}
```

#### Environment To Bindable
When accessing @Observable from environment, create local @Bindable for bindings:

```swift
struct SidebarView: View {
    @Environment(AppState.self) private var appState

    var body: some View {
        // Create local @Bindable for bindings
        @Bindable var appState = appState

        List(appState.items, selection: $appState.selectedID) { item in
            Text(item.name)
        }
    }
}
```

### Navigation
### Navigation Split View
Standard three-column layout:

```swift
struct ContentView: View {
    @State private var selectedFolder: Folder?
    @State private var selectedItem: Item?

    var body: some View {
        NavigationSplitView {
            // Sidebar
            SidebarView(selection: $selectedFolder)
        } content: {
            // Content list
            if let folder = selectedFolder {
                ItemListView(folder: folder, selection: $selectedItem)
            } else {
                ContentUnavailableView("Select a Folder", systemImage: "folder")
            }
        } detail: {
            // Detail
            if let item = selectedItem {
                DetailView(item: item)
            } else {
                ContentUnavailableView("Select an Item", systemImage: "doc")
            }
        }
        .navigationSplitViewColumnWidth(min: 180, ideal: 200, max: 300)
    }
}
```

### Two Column Layout
```swift
struct ContentView: View {
    @State private var selectedItem: Item?

    var body: some View {
        NavigationSplitView {
            SidebarView(selection: $selectedItem)
                .navigationSplitViewColumnWidth(min: 200, ideal: 250)
        } detail: {
            if let item = selectedItem {
                DetailView(item: item)
            } else {
                ContentUnavailableView("No Selection", systemImage: "sidebar.left")
            }
        }
    }
}
```

### Navigation Stack
For drill-down navigation:

```swift
struct BrowseView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            CategoryListView()
                .navigationDestination(for: Category.self) { category in
                    ItemListView(category: category)
                }
                .navigationDestination(for: Item.self) { item in
                    DetailView(item: item)
                }
        }
    }
}
```

### Windows
### Multiple Window Types
```swift
@main
struct MyApp: App {
    var body: some Scene {
        // Main window
        WindowGroup {
            ContentView()
        }
        .commands {
            AppCommands()
        }

        // Auxiliary window
        Window("Inspector", id: "inspector") {
            InspectorView()
        }
        .windowResizability(.contentSize)
        .defaultPosition(.trailing)
        .keyboardShortcut("i", modifiers: [.command, .option])

        // Utility window
        Window("Quick Entry", id: "quick-entry") {
            QuickEntryView()
        }
        .windowStyle(.hiddenTitleBar)
        .windowResizability(.contentSize)

        // Settings
        Settings {
            SettingsView()
        }
    }
}
```

### Window Control
Open windows programmatically:

```swift
struct ContentView: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Show Inspector") {
            openWindow(id: "inspector")
        }
    }
}
```

### Document Group
For document-based apps:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: MyDocument()) { file in
            DocumentView(document: file.$document)
        }
        .commands {
            DocumentCommands()
        }
    }
}
```

### Debugging Swiftui Appkit
**Meta-principle: Declarative overrides Imperative**

When SwiftUI wraps AppKit (via NSHostingView, NSViewRepresentable, etc.), SwiftUI's declarative layer manages the AppKit objects underneath. Your AppKit code may be "correct" but irrelevant if SwiftUI is controlling that concern.

**Debugging pattern:**
1. Issue occurs (e.g., window won't respect constraints, focus not working, layout broken)
2. ❌ **Wrong approach:** Jump to AppKit APIs to "fix" it imperatively
3. ✅ **Right approach:** Check SwiftUI layer first - what's declaratively controlling this?
4. **Why:** The wrapper controls the wrapped. Higher abstraction wins.

**Example scenario - Window sizing:**
- Symptom: `NSWindow.minSize` code runs but window still resizes smaller
- Wrong: Add more AppKit code, observers, notifications to "force" it
- Right: Search codebase for `.frame(minWidth:)` on content view - that's what's actually controlling it
- Lesson: NSHostingView manages window constraints based on SwiftUI content

**This pattern applies broadly:**
- Window sizing → Check `.frame()`, `.windowResizability()` before `NSWindow` properties
- Focus management → Check `@FocusState`, `.focused()` before `NSResponder` chain
- Layout constraints → Check SwiftUI layout modifiers before Auto Layout
- Toolbar → Check `.toolbar {}` before `NSToolbar` setup

**When to actually use AppKit:**
Only when SwiftUI doesn't provide the capability (custom drawing, specialized controls, backward compatibility). Not as a workaround when SwiftUI "doesn't work" - you probably haven't found SwiftUI's way yet.

### Toolbar
### Toolbar Content
```swift
struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        NavigationSplitView {
            SidebarView()
        } detail: {
            DetailView()
        }
        .toolbar {
            ToolbarItemGroup(placement: .primaryAction) {
                Button(action: addItem) {
                    Label("Add", systemImage: "plus")
                }

                Button(action: deleteItem) {
                    Label("Delete", systemImage: "trash")
                }
            }

            ToolbarItem(placement: .navigation) {
                Button(action: toggleSidebar) {
                    Label("Toggle Sidebar", systemImage: "sidebar.left")
                }
            }
        }
        .searchable(text: $searchText, placement: .toolbar)
    }

    private func toggleSidebar() {
        NSApp.keyWindow?.firstResponder?.tryToPerform(
            #selector(NSSplitViewController.toggleSidebar(_:)),
            with: nil
        )
    }
}
```

### Customizable Toolbar
```swift
struct ContentView: View {
    var body: some View {
        MainContent()
            .toolbar(id: "main") {
                ToolbarItem(id: "add", placement: .primaryAction) {
                    Button(action: add) {
                        Label("Add", systemImage: "plus")
                    }
                }

                ToolbarItem(id: "share", placement: .secondaryAction) {
                    ShareLink(item: currentItem)
                }

                ToolbarItem(id: "spacer", placement: .automatic) {
                    Spacer()
                }
            }
            .toolbarRole(.editor)
    }
}
```

### Menus
### App Commands
```swift
struct AppCommands: Commands {
    @Environment(\.openWindow) private var openWindow

    var body: some Commands {
        // Replace standard menu items
        CommandGroup(replacing: .newItem) {
            Button("New Project") {
                // Create new project
            }
            .keyboardShortcut("n", modifiers: .command)
        }

        // Add new menu
        CommandMenu("View") {
            Button("Show Inspector") {
                openWindow(id: "inspector")
            }
            .keyboardShortcut("i", modifiers: [.command, .option])

            Divider()

            Button("Zoom In") {
                // Zoom in
            }
            .keyboardShortcut("+", modifiers: .command)

            Button("Zoom Out") {
                // Zoom out
            }
            .keyboardShortcut("-", modifiers: .command)
        }

        // Add to existing menu
        CommandGroup(after: .sidebar) {
            Button("Toggle Inspector") {
                // Toggle
            }
            .keyboardShortcut("i", modifiers: .command)
        }
    }
}
```

### Context Menus
```swift
struct ItemRow: View {
    let item: Item
    let onDelete: () -> Void
    let onDuplicate: () -> Void

    var body: some View {
        HStack {
            Text(item.name)
            Spacer()
        }
        .contextMenu {
            Button("Duplicate") {
                onDuplicate()
            }

            Button("Delete", role: .destructive) {
                onDelete()
            }

            Divider()

            Menu("Move to") {
                ForEach(folders) { folder in
                    Button(folder.name) {
                        move(to: folder)
                    }
                }
            }
        }
    }
}
```

### Lists And Tables
### List Selection
```swift
struct SidebarView: View {
    @Environment(AppState.self) private var appState

    var body: some View {
        @Bindable var appState = appState

        List(appState.items, selection: $appState.selectedItemID) { item in
            Label(item.name, systemImage: item.icon)
                .tag(item.id)
        }
        .listStyle(.sidebar)
    }
}
```

### Table
```swift
struct ItemTableView: View {
    @Environment(AppState.self) private var appState
    @State private var sortOrder = [KeyPathComparator(\Item.name)]

    var body: some View {
        @Bindable var appState = appState

        Table(appState.items, selection: $appState.selectedItemIDs, sortOrder: $sortOrder) {
            TableColumn("Name", value: \.name) { item in
                Text(item.name)
            }

            TableColumn("Date", value: \.createdAt) { item in
                Text(item.createdAt.formatted(date: .abbreviated, time: .shortened))
            }
            .width(min: 100, ideal: 150)

            TableColumn("Size", value: \.size) { item in
                Text(ByteCountFormatter.string(fromByteCount: item.size, countStyle: .file))
            }
            .width(80)
        }
        .onChange(of: sortOrder) {
            appState.items.sort(using: sortOrder)
        }
    }
}
```

### Outline Group
For hierarchical data:

```swift
struct OutlineView: View {
    let rootItems: [TreeItem]

    var body: some View {
        List {
            OutlineGroup(rootItems, children: \.children) { item in
                Label(item.name, systemImage: item.icon)
            }
        }
    }
}

struct TreeItem: Identifiable {
    let id = UUID()
    var name: String
    var icon: String
    var children: [TreeItem]?
}
```

### Forms
### Settings Form
```swift
struct SettingsView: View {
    @AppStorage("autoSave") private var autoSave = true
    @AppStorage("saveInterval") private var saveInterval = 5
    @AppStorage("theme") private var theme = "system"

    var body: some View {
        Form {
            Section("General") {
                Toggle("Auto-save documents", isOn: $autoSave)

                if autoSave {
                    Stepper("Save every \(saveInterval) minutes", value: $saveInterval, in: 1...60)
                }
            }

            Section("Appearance") {
                Picker("Theme", selection: $theme) {
                    Text("System").tag("system")
                    Text("Light").tag("light")
                    Text("Dark").tag("dark")
                }
                .pickerStyle(.radioGroup)
            }
        }
        .formStyle(.grouped)
        .frame(width: 400)
        .padding()
    }
}
```

### Validation
```swift
struct EditItemView: View {
    @Binding var item: Item
    @State private var isValid = true

    var body: some View {
        Form {
            TextField("Name", text: $item.name)
                .onChange(of: item.name) {
                    isValid = !item.name.isEmpty
                }

            if !isValid {
                Text("Name is required")
                    .foregroundStyle(.red)
                    .font(.caption)
            }
        }
    }
}
```

### Sheets And Alerts
### Sheet
```swift
struct ContentView: View {
    @State private var showingSheet = false
    @State private var itemToEdit: Item?

    var body: some View {
        MainContent()
            .sheet(isPresented: $showingSheet) {
                SheetContent()
            }
            .sheet(item: $itemToEdit) { item in
                EditItemView(item: item)
            }
    }
}
```

### Confirmation Dialog
```swift
struct ItemRow: View {
    let item: Item
    @State private var showingDeleteConfirmation = false

    var body: some View {
        Text(item.name)
            .confirmationDialog(
                "Delete \(item.name)?",
                isPresented: $showingDeleteConfirmation,
                titleVisibility: .visible
            ) {
                Button("Delete", role: .destructive) {
                    deleteItem()
                }
            } message: {
                Text("This action cannot be undone.")
            }
    }
}
```

### File Dialogs
```swift
struct ContentView: View {
    @State private var showingImporter = false
    @State private var showingExporter = false

    var body: some View {
        VStack {
            Button("Import") {
                showingImporter = true
            }
            Button("Export") {
                showingExporter = true
            }
        }
        .fileImporter(
            isPresented: $showingImporter,
            allowedContentTypes: [.json, .plainText],
            allowsMultipleSelection: true
        ) { result in
            switch result {
            case .success(let urls):
                importFiles(urls)
            case .failure(let error):
                handleError(error)
            }
        }
        .fileExporter(
            isPresented: $showingExporter,
            document: exportDocument,
            contentType: .json,
            defaultFilename: "export.json"
        ) { result in
            // Handle result
        }
    }
}
```

### Drag And Drop
### Draggable
```swift
struct DraggableItem: View {
    let item: Item

    var body: some View {
        Text(item.name)
            .draggable(item.id.uuidString) {
                // Preview
                Label(item.name, systemImage: item.icon)
                    .padding()
                    .background(.regularMaterial)
                    .cornerRadius(8)
            }
    }
}
```

### Drop Target
```swift
struct DropTargetView: View {
    @State private var isTargeted = false

    var body: some View {
        Rectangle()
            .fill(isTargeted ? Color.accentColor.opacity(0.3) : Color.clear)
            .dropDestination(for: String.self) { items, location in
                for itemID in items {
                    handleDrop(itemID)
                }
                return true
            } isTargeted: { targeted in
                isTargeted = targeted
            }
    }
}
```

### Reorderable List
```swift
struct ReorderableList: View {
    @State private var items = ["A", "B", "C", "D"]

    var body: some View {
        List {
            ForEach(items, id: \.self) { item in
                Text(item)
            }
            .onMove { from, to in
                items.move(fromOffsets: from, toOffset: to)
            }
        }
    }
}
```

### Focus And Keyboard
### Focus State
```swift
struct EditForm: View {
    @State private var name = ""
    @State private var description = ""
    @FocusState private var focusedField: Field?

    enum Field {
        case name, description
    }

    var body: some View {
        Form {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)

            TextField("Description", text: $description)
                .focused($focusedField, equals: .description)
        }
        .onSubmit {
            switch focusedField {
            case .name:
                focusedField = .description
            case .description:
                save()
            case nil:
                break
            }
        }
        .onAppear {
            focusedField = .name
        }
    }
}
```

#### Keyboard Shortcuts
**CRITICAL: Menu commands required for reliable keyboard shortcuts**

`.onKeyPress()` handlers ALONE are unreliable in SwiftUI. You MUST define menu commands with `.keyboardShortcut()` for keyboard shortcuts to work properly.

### Correct Pattern
**Step 1: Define menu command in App or WindowGroup:**

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .commands {
            CommandMenu("Edit") {
                EditLoopButton()
                Divider()
                DeleteButton()
            }
        }
    }
}

// Menu command buttons with keyboard shortcuts
struct EditLoopButton: View {
    @FocusedValue(\.selectedItem) private var selectedItem

    var body: some View {
        Button("Edit Item") {
            // Perform action
        }
        .keyboardShortcut("e", modifiers: [])
        .disabled(selectedItem == nil)
    }
}

struct DeleteButton: View {
    @FocusedValue(\.selectedItem) private var selectedItem

    var body: some View {
        Button("Delete Item") {
            // Perform deletion
        }
        .keyboardShortcut(.delete, modifiers: [])
        .disabled(selectedItem == nil)
    }
}
```

**Step 2: Expose state via FocusedValues:**

```swift
// Define focused value keys
struct SelectedItemKey: FocusedValueKey {
    typealias Value = Binding<Item?>
}

extension FocusedValues {
    var selectedItem: Binding<Item?>? {
        get { self[SelectedItemKey.self] }
        set { self[SelectedItemKey.self] = newValue }
    }
}

// In your view, expose the state
struct ContentView: View {
    @State private var selectedItem: Item?

    var body: some View {
        ItemList(selection: $selectedItem)
            .focusedSceneValue(\.selectedItem, $selectedItem)
    }
}
```

**Why menu commands are required:**
- `.keyboardShortcut()` on menu buttons registers shortcuts at the system level
- `.onKeyPress()` alone only works when the view hierarchy receives events
- System menus (Edit, View, etc.) can intercept keys before `.onKeyPress()` fires
- Menu commands show shortcuts in the menu bar for discoverability


### Onkeypress Usage
**When to use `.onKeyPress()`:**

Use for keyboard **input** (typing, arrow keys for navigation):

```swift
struct ContentView: View {
    @FocusState private var isInputFocused: Bool

    var body: some View {
        MainContent()
            .onKeyPress(.upArrow) {
                guard !isInputFocused else { return .ignored }
                selectPrevious()
                return .handled
            }
            .onKeyPress(.downArrow) {
                guard !isInputFocused else { return .ignored }
                selectNext()
                return .handled
            }
            .onKeyPress(characters: .alphanumerics) { press in
                guard !isInputFocused else { return .ignored }
                handleTypeahead(press.characters)
                return .handled
            }
    }
}
```

**Always check focus state** to prevent interfering with text input.

### Previews
```swift
#Preview("Default") {
    ContentView()
        .environment(AppState())
}

#Preview("With Data") {
    let state = AppState()
    state.items = [
        Item(name: "First"),
        Item(name: "Second")
    ]

    return ContentView()
        .environment(state)
}

#Preview("Dark Mode") {
    ContentView()
        .environment(AppState())
        .preferredColorScheme(.dark)
}

#Preview(traits: .fixedLayout(width: 800, height: 600)) {
    ContentView()
        .environment(AppState())
}
```
