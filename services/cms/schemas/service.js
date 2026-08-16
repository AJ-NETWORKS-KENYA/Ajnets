/**
 * Sanity Schema: Service (Practice Areas & Consulting Capabilities)
 */
export default {
  name: 'service',
  title: 'Practice Area / Service',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Practice Title',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: { source: 'title', maxLength: 96 },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'tagline',
      title: 'Value Proposition Tagline',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'overview',
      title: 'Overview Description',
      type: 'text',
      rows: 4,
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'capabilities',
      title: 'Core Capabilities & Deliverables',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            { name: 'heading', title: 'Capability Title', type: 'string', validation: (R) => R.required() },
            { name: 'description', title: 'Capability Details', type: 'text', rows: 2, validation: (R) => R.required() },
          ],
        },
      ],
    },
    {
      name: 'faqs',
      title: 'Service FAQs',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            { name: 'question', title: 'Question', type: 'string', validation: (R) => R.required() },
            { name: 'answer', title: 'Answer', type: 'text', rows: 3, validation: (R) => R.required() },
          ],
        },
      ],
    },
  ],
};
