/**
 * Sanity Schema: Case Study (Client Engagements & Delivery Proof)
 */
export default {
  name: 'caseStudy',
  title: 'Case Study',
  type: 'document',
  fields: [
    {
      name: 'clientName',
      title: 'Client / Project Name',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'clientName',
        maxLength: 96,
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'industry',
      title: 'Industry Vertical',
      type: 'string',
      options: {
        list: [
          'Fintech & Digital Banking',
          'Healthcare & Medical Funds',
          'Education & EdTech',
          'Logistics & Supply Chain',
          'E-Commerce & Retail',
          'Non-Profit & Community',
        ],
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'servicePractice',
      title: 'Primary Service Practice',
      type: 'reference',
      to: [{ type: 'service' }],
    },
    {
      name: 'summary',
      title: 'Executive Summary',
      type: 'text',
      rows: 3,
      validation: (Rule) => Rule.required().max(200),
    },
    {
      name: 'challenge',
      title: 'Business Challenge & Scope',
      type: 'text',
      rows: 4,
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'solution',
      title: 'Engineering Solution & Architecture',
      type: 'array',
      of: [{ type: 'block' }],
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'metrics',
      title: 'Quantifiable Results & Metrics',
      type: 'array',
      of: [
        {
          type: 'object',
          fields: [
            { name: 'value', title: 'Metric Value (e.g. 99.9%, 40% Reduction)', type: 'string', validation: (R) => R.required() },
            { name: 'label', title: 'Metric Label (e.g. Uptime SLA, Query Latency)', type: 'string', validation: (R) => R.required() },
          ],
        },
      ],
    },
    {
      name: 'coverImage',
      title: 'Case Study Hero / Showcase Image',
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
      validation: (Rule) => Rule.required(),
    },
  ],
  preview: {
    select: {
      title: 'clientName',
      subtitle: 'industry',
      media: 'coverImage',
    },
  },
};
