/**
 * Sanity Schema: Team Member / Consultant Author
 */
export default {
  name: 'teamMember',
  title: 'Team Member',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Full Name',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'role',
      title: 'Role / Designation',
      type: 'string',
      validation: (Rule) => Rule.required(),
    },
    {
      name: 'bio',
      title: 'Short Bio',
      type: 'text',
      rows: 3,
    },
    {
      name: 'avatar',
      title: 'Profile Picture',
      type: 'image',
      options: { hotspot: true },
      fields: [
        { name: 'alt', title: 'Alt Text', type: 'string' }
      ]
    },
    {
      name: 'linkedin',
      title: 'LinkedIn Profile URL',
      type: 'url',
    },
  ],
};
