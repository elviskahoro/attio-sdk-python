# OpenAPI Overlay Guide

## Overview

This guide documents how to create and use OpenAPI Overlays for customizing API specifications without modifying the original OpenAPI document. Based on the Speakeasy API implementation patterns, this guide provides a reference for building overlays that sit on top of your OpenAPI specification.

## What are OpenAPI Overlays?

OpenAPI Overlays are separate YAML documents that define modifications to be applied to an existing OpenAPI specification. They follow the [OpenAPI Overlay Specification v1.0.0](https://github.com/OAI/Overlay-Specification) and allow you to:

- Add or modify API metadata and descriptions
- Inject code samples and examples
- Add Speakeasy-specific extensions
- Hide internal endpoints from public SDKs
- Standardize configurations across operations
- Customize SDK generation behavior

## Why Use Overlays?

Overlays provide several key benefits:

1. **Separation of concerns**: Keep API definition separate from SDK-specific customizations
2. **Non-invasive**: Apply modifications without editing the upstream OpenAPI document
3. **Reusability**: Apply the same overlay to multiple OpenAPI documents
4. **Version control**: Track customizations independently from the core API spec
5. **Team collaboration**: Different teams can maintain overlays for different purposes

## Overlay Document Structure

### Basic Anatomy

Every overlay document contains three required sections:

```yaml
overlay: 1.0.0              # Overlay specification version
info:                        # Metadata about the overlay
  title: "Description"
  version: "0.0.1"
actions:                     # Array of modifications to apply
  - target: "JSONPath"
    update: {}
```

### Components Breakdown

#### 1. Overlay Version
```yaml
overlay: 1.0.0
```
Specifies the Overlay Specification version. Currently limited to `1.0.0`.

#### 2. Info Object
```yaml
info:
  title: "Fix generateCodeSamplePreviewAsync method name"
  version: "0.0.1"
```
- **title** (required): Human-readable description of the overlay's purpose
- **version** (required): Version identifier for the overlay document

#### 3. Actions Array
```yaml
actions:
  - target: "$.paths.*.*[?(@.operationId == 'generateCodeSamplePreviewAsync')]"
    description: "Optional description of this action"
    update:
      x-speakeasy-name-override: generateCodeSamplePreviewAsynchronous
```

Each action contains:
- **target** (required): JSONPath expression identifying where to apply changes
- **description** (optional): Explanation of the action (supports CommonMark syntax)
- **update** (optional): Properties and values to merge with target objects
- **remove** (optional): Boolean to remove the target object (default: false)

## JSONPath Expressions

JSONPath expressions locate specific parts of the OpenAPI document to modify.

### Common Patterns

| Expression | Description |
|------------|-------------|
| `$.info.title` | Select the title field of the info object |
| `$.servers[0].url` | Select the URL of the first server |
| `$.paths['/drinks'].get` | Select the GET operation on /drinks path |
| `$.paths.*.*` | Select all operations across all paths |
| `$.paths..parameters[?(@.in=='query')]` | Select all query parameters |
| `$.components.schemas.Drink` | Select the Drink schema |
| `$.paths.*[?(@.operationId == 'listUsers')]` | Select operations by operationId |

### Target Selection Guidelines

| Update Type | Target Object |
|-------------|---------------|
| Update primitive value (string, number, boolean) | The containing object |
| Update an object | The object itself |
| Update an array | The array itself |
| Add new property to object | The object itself |
| Add new item to array | The array itself |
| Remove property from object | The object itself |
| Remove item from array | The array itself |

## Common Overlay Use Cases

### 1. Adding Code Samples

Inject language-specific code examples into your API documentation:

```yaml
overlay: 1.0.0
info:
  title: CodeSamples overlay for python target
  version: 0.0.0
actions:
  - target: $["paths"]["/v1/artifacts/namespaces"]["get"]
    update:
      x-codeSamples:
        - lang: python
          label: getNamespaces
          source: |-
            from speakeasy_client_sdk_python import Speakeasy
            from speakeasy_client_sdk_python.models import shared

            with Speakeasy(
                security=shared.Security(
                    api_key="<YOUR_API_KEY_HERE>",
                ),
            ) as speakeasy:
                res = speakeasy.artifacts.get_namespaces()
                assert res.get_namespaces_response is not None
                print(res.get_namespaces_response)
```

### 2. Method Name Overrides

Customize generated SDK method names:

```yaml
overlay: 1.0.0
info:
  title: Fix generateCodeSamplePreviewAsync method name
  version: 0.0.1
actions:
  - target: $.paths.*.*[?(@.operationId == 'generateCodeSamplePreviewAsync')]
    update:
      x-speakeasy-name-override: generateCodeSamplePreviewAsynchronous
```

### 3. Adding Speakeasy Extensions

Enable Terraform provider support or other Speakeasy features:

```yaml
overlay: 1.0.0
info:
  title: Add Terraform Functionality to Order Schema
  version: 1.1.0
actions:
  - target: "$.components.schemas.Order"
    update:
      x-speakeasy-entity: Order
```

### 4. Hiding Internal APIs

Exclude internal endpoints from public SDK generation:

```yaml
overlay: 1.0.0
info:
  title: Secure Internal Staff Management Endpoint
  version: 1.1.4
actions:
  - target: "$.paths['/internal/staff']"
    update:
      x-internal: true
```

### 5. Adding Examples

Provide concrete examples to clarify API usage:

```yaml
overlay: 1.0.0
info:
  title: Add Drink Order Example for User Clarity
  version: 1.1.3
actions:
  - target: "$.paths['/drinks/order'].post"
    update:
      examples:
        standardOrder:
          summary: "Standard order example"
          value:
            drink: "Old Fashioned"
            quantity: 1
```

### 6. Standardizing Configurations

Remove operation-level server and security configurations to use global defaults:

```yaml
overlay: 1.0.0
info:
  title: Standardize Server and Security Configurations
  version: 1.1.0
actions:
  - target: $.paths.*.*.servers
    remove: true
  - target: $.paths.*.*.security
    remove: true
```

### 7. Removing Deprecated Operations

Remove operations marked as deprecated:

```yaml
overlay: 1.0.0
info:
  title: Remove Deprecated Drink Operations
  version: 1.1.0
actions:
  - target: $.paths['/drinks'].*.deprecated
    remove: true
  - target: $.paths['/drinks/{drinkId}'].*.deprecated
    remove: true
```

### 8. Removing Specific Operations

Remove operations that don't have specific extensions:

```yaml
overlay: 1.0.0
info:
  title: Remove Non-Essential PUT Operations
  version: 1.1.0
actions:
  - target: $.paths.*.put[?(! @.x-speakeasy-entity-operation)]
    remove: true
```

### 9. Adding SDK-Specific Documentation

Provide tailored instructions for different SDK languages:

```yaml
overlay: 1.0.0
info:
  title: Distinguish Order Endpoint Docs for Java and JavaScript SDKs
  version: 1.1.1
actions:
  - target: "$.paths['/orders'].post.description"
    update:
      value: "For Java SDK: use `OrderService.placeOrder()`. For JavaScript SDK: use `orderService.placeOrder()`."
```

### 10. Enhancing Schema Definitions

Add more descriptive properties to autogenerated schemas:

```yaml
overlay: 1.0.0
info:
  title: Refine Drink Schema for Better Clarity
  version: 1.1.2
actions:
  - target: "$.components.schemas.Drink"
    update:
      properties:
        type:
          type: string
          description: "Type of drink, e.g., 'cocktail', 'beer'."
        alcoholContent:
          type: number
          description: "Percentage of alcohol by volume."
```

## Working with Overlays

### Creating an Overlay

**Option 1: Manual Creation**

Write a YAML file following the overlay structure defined above.

**Option 2: Generate from Differences**

Use the Speakeasy CLI to compare two versions of an OpenAPI document:

```bash
speakeasy overlay compare --before=./openapi_original.yaml --after=./openapi.yaml > overlay.yaml
```

### Validating an Overlay

Ensure your overlay adheres to the specification:

```bash
speakeasy overlay validate -o overlay.yaml
```

### Applying an Overlay

**Option 1: Add to Speakeasy Workflow**

Configure the overlay in your `.speakeasy/workflow.yaml` to automatically apply during SDK generation:

```bash
speakeasy configure sources
# Select your source and add the overlay file path when prompted
```

Then run:
```bash
speakeasy run
```

**Option 2: Generate New OpenAPI Document**

Create a combined OpenAPI document with the overlay applied:

```bash
speakeasy overlay apply -s openapi.yaml -o overlay.yaml > combined.yaml
```

## Speakeasy-Specific Extensions

Common Speakeasy extensions you can add via overlays:

- `x-speakeasy-name-override`: Override generated method/class names
- `x-speakeasy-entity`: Enable Terraform provider support
- `x-speakeasy-entity-operation`: Mark operations for entity support
- `x-internal`: Hide endpoints from public SDK generation
- `x-codeSamples`: Add language-specific code examples
- `x-speakeasy-retries`: Configure retry behavior
- `x-speakeasy-pagination`: Configure pagination handling

## Best Practices

1. **Use descriptive titles and descriptions**: Make it clear what each overlay and action does
2. **Version your overlays**: Track changes to overlays alongside your API versions
3. **Test JSONPath expressions**: Use tools like [jsonpath.com](https://jsonpath.com/) to validate expressions
4. **Keep overlays focused**: Create separate overlays for different concerns (code samples, extensions, hiding endpoints)
5. **Document your overlays**: Add comments and descriptions to explain why modifications are needed
6. **Validate before applying**: Always run `speakeasy overlay validate` before use
7. **Use the visual playground**: Try [overlay.speakeasy.com](https://overlay.speakeasy.com/) for interactive overlay creation

## Implementation Workflow

1. **Identify customization needs**: Determine what modifications are required for SDK generation
2. **Create overlay file**: Write the overlay YAML with appropriate actions
3. **Validate overlay**: Run validation to catch errors early
4. **Test locally**: Apply overlay and review the combined output
5. **Integrate with workflow**: Add to Speakeasy configuration for automatic application
6. **Version control**: Commit overlay to version control alongside OpenAPI spec
7. **Document changes**: Maintain changelog of overlay modifications

## Troubleshooting

### Common Issues

**JSONPath not matching**: Validate your JSONPath expression using online tools or by testing on a sample of your OpenAPI document.

**Overlay not applying**: Ensure the `target` is pointing to the correct location and that the overlay format follows the specification.

**Conflicts between actions**: Actions are applied in order. Ensure later actions don't conflict with earlier ones.

**Extensions not recognized**: Verify you're using the correct Speakeasy extension names and syntax.

## Tools and Resources

- **Speakeasy CLI**: Install with `brew install speakeasy-api/tap/speakeasy`
- **Visual Overlay Editor**: [overlay.speakeasy.com](https://overlay.speakeasy.com/)
- **JSONPath Tester**: [jsonpath.com](https://jsonpath.com/)
- **OpenAPI Overlay Spec**: [GitHub Repository](https://github.com/OAI/Overlay-Specification)
- **Speakeasy Overlay Implementation**: [GitHub](https://github.com/speakeasy-api/openapi-overlay)

## Example Reference Implementation

The Speakeasy Python SDK uses two primary overlay files:

1. **overlay.yaml**: Fixes method naming issues
2. **codeSamples.yaml**: Injects Python code samples for all endpoints

These files are referenced in `.speakeasy/gen.yaml` and applied automatically during SDK generation.

## Conclusion

OpenAPI Overlays provide a powerful, non-invasive way to customize API specifications for SDK generation. By maintaining overlays separately from your core OpenAPI document, you can:

- Keep your API specification clean and focused
- Apply SDK-specific customizations without modifying the source
- Maintain different overlays for different SDK targets or use cases
- Version control customizations independently

Use this guide as a reference when building overlays for your own API specifications.
