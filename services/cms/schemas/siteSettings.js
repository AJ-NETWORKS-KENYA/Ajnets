/**
 * Sanity Schema: Site Settings (Singleton)
 */
export default {
  name: 'siteSettings',
  title: 'Global Site Settings',
  type: 'document',
  fields: [
    {
      name: 'siteName',
      title: 'Company / Brand Name',
      type: 'string',
      initialValue: 'AJNETWORKS',
    },
    {
      name: 'siteUrl',
      title: 'Canonical Base URL',
      type: 'url',
      initialValue: 'https://ajnetworks.co',
    },
    {
      name: 'contactEmail',
      title: 'Support / Inquiry Email',
      type: 'string',
      initialValue: 'hello@ajnetworks.co',
    },
    {
      name: 'contactPhone',
      title: 'Phone Number',
      type: 'string',
      initialValue: '+254 758 238 617',
    },
    {
      name: 'headquarters',
      title: 'Headquarters Address',
      type: 'string',
      initialValue: 'Nairobi & Mombasa, Kenya',
    },
    {
      name: 'defaultMetaDescription',
      title: 'Default Meta Description',
      type: 'text',
      rows: 3,
    },
  ],
};
