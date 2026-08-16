/**
 * Sanity Schema: Post (Tech Insights & Perspective Articles)
 */
export default {
  name: 'post',
  title: 'Insight Article',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Article Title',
      type: 'string',
      description: 'Engaging, intent-rich title for search visibility (under 65 characters).',
      validation: (Rule) => Rule.required().max(65).warning('Shorter titles rank better in search results.'),
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96,
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'category',
      title: 'Practice Area / Category',
      type: 'string',
      options: {
        list: [
          { title: 'Technology & Digital Strategy', value: 'technology-strategy' },
          { title: 'Custom Software Engineering', value: 'software-engineering' },
          { title: 'Cybersecurity & Assurance', value: 'cybersecurity' },
          { title: 'Infrastructure & Networking', value: 'networking' },
          { title: 'Performance & Technical SEO', value: 'performance-seo' },
        ],
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'author',
      title: 'Author',
      type: 'reference',
      to: [{ type: 'teamMember' }],
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'publishedAt',
      title: 'Published Date',
      type: 'datetime',
      initialValue: () => new Date().toISOString(),
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'excerpt',
      title: 'Meta Description & Article Excerpt',
      type: 'text',
      rows: 3,
      description: 'Concise summary for search engines and social cards (140-160 characters).',
      validation: (Rule) =>
        Rule.required()
          .min(100)
          .max(160)
          .warning('Optimal meta descriptions are between 140 and 160 characters.'),
    },
    {
      name: 'mainImage',
      title: 'Cover Image',
      type: 'image',
      options: {
        hotspot: true,
      },
      fields: [
        {
          name: 'alt',
          type: 'string',
          title: 'Alternative Text (Alt)',
          description: 'Critical for accessibility and SEO ranking.',
          validation: (Rule) => Rule.required(),
        },
        {
          name: 'caption',
          type: 'string',
          title: 'Caption',
        },
      ],
    },
    {
      name: 'body',
      title: 'Article Body',
      type: 'array',
      of: [
        {
          type: 'block',
          styles: [
            { title: 'Normal', value: 'normal' },
            { title: 'H2 (Section Heading)', value: 'h2' },
            { title: 'H3 (Sub-heading)', value: 'h3' },
            { title: 'Quote', value: 'blockquote' },
          ],
        },
        {
          type: 'image',
          options: { hotspot: true },
          fields: [
            {
              name: 'alt',
              type: 'string',
              title: 'Alt Text',
              validation: (Rule) => Rule.required(),
            },
          ],
        },
      ],
    },
  ],
  preview: {
    select: {
      title: 'title',
      author: 'author.name',
      media: 'mainImage',
    },
    prepare(selection) {
      const { author } = selection;
      return Object.assign({}, selection, {
        subtitle: author && `by ${author}`,
      });
    },
  },
};
