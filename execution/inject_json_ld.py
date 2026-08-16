import os

org_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "AJNETWORKS",
  "image": "https://ajnetworks.co/images/logo.svg",
  "@id": "https://ajnetworks.co/",
  "url": "https://ajnetworks.co/",
  "telephone": "+254700000000",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Nairobi",
    "addressLocality": "Nairobi",
    "addressCountry": "KE"
  }
}
</script>
"""

article_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AJNETWORKS Case Study & Insight",
  "image": "https://ajnetworks.co/images/og-home.webp",
  "author": {
    "@type": "Person",
    "name": "Abraham John"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AJNETWORKS",
    "logo": {
      "@type": "ImageObject",
      "url": "https://ajnetworks.co/images/logo.svg"
    }
  }
}
</script>
"""

service_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "AJNETWORKS Consulting Service",
  "provider": {
    "@type": "Organization",
    "name": "AJNETWORKS"
  }
}
</script>
"""

def inject(filepath, schema_type, schema):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if f'"@type": "{schema_type}"' in content:
        return
    new_content = content.replace('</head>', schema + '\n</head>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Injected {schema_type} JSON-LD into {filepath}")

def main():
    base_dir = r"c:\My Web Sites\ajnets"
    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                
                # Assign schemas based on folder
                if 'portfolio' in path or 'insights' in path:
                    inject(path, "Article", article_schema)
                elif 'services' in path:
                    inject(path, "Service", service_schema)

if __name__ == "__main__":
    main()
