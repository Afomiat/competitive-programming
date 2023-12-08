class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain = {}

        for cpdomain in cpdomains:
            dom_val, dom_name = cpdomain.split(" ")
            val = int(dom_val)

            if dom_name in domain:
                domain[dom_name] += val
            else:
                domain[dom_name] = val

            # left = 0
            for i in range(len(dom_name)):
                if dom_name[i] == ".":
                    subdomain = dom_name[i + 1:]
                    if subdomain in domain:
                        domain[subdomain] += val
                    else:
                        domain[subdomain] = val

        result = ["{} {}".format(val, key) for key, val in domain.items()]

        return result